#! /usr/bin/env roseus

(load "pose-model.l")
(ros::roseus-add-msgs "trajectory_msgs")
(ros::roseus "2d-listener" :anonymous t)

(defvar joint-list)

(defun change-joint (name angle)
  (format t "joint name = ~A , angle degree ~A%" name angle)
  (cond ((equal name "r-shoulder") (send *2d-model* :r-shoulder angle)))
  (cond ((equal name "r-elbow") (print angle)))
  (cond ((equal name "l-shoulder") (print angle)))
  (cond ((equal name "l-elbow") (print 4)))
  (cond ((equal name "r-hip-joint") (print 6)))
  (cond ((equal name "r-knee") (print 7)))
  (cond ((equal name "l-hip-joint") (print 8)))
  (cond ((equal name "l-knee") (print 9)))
  )

(defun cb (msg)
  (setq name-list (send msg :joint_names))
  (setq angle-list (send (elt (send msg :points) 0) :positions))
  (dotimes (i (length joint-list)) (change-joint (elt name-list i) (elt angle-list i)))
  ; (dolist (joint joint-list) (change-joint joint))
  )

(ros::subscribe "/2d_human_joint" trajectory_msgs::JointTrajectory #'cb)

(setq *2d-model* (instance 2d-pose-model :init))
(objects *2d-model*)
(send *2d-model* :angle-vector #f(20 30 -20 -30 40 30 -40 -30))

(ros::rate 10)
(while (ros::ok)
  (print 1)
  ;;(ros::ros-info "")
  (ros::spin-once)
  (ros::sleep))
(exit)
