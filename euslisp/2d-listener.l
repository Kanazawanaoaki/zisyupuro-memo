#!/usr/bin/env roseus

(load "pose-model.l")

(ros::roseus-add-msgs "trajectory_msgs")
(ros::roseus "2d_listener" :anonymous t)

(defvar joint-list)

(defun change-joint (name angle)
  (format t "joint name = ~A , angle degree ~A~%" name angle)
  (cond ((equal name "r-shoulder") (send *2d-model* :r-shoulder angle)))
  (cond ((equal name "r-elbow") (send *2d-model* :r-elbow angle)))
  (cond ((equal name "l-shoulder") (send *2d-model* :l-shoulder angle)))
  (cond ((equal name "l-elbow") (send *2d-model* :l-elbow angle)))
  (cond ((equal name "r-hip-joint") (send *2d-model* :r-hip angle)))
  (cond ((equal name "r-knee") (send *2d-model* :r-knee angle)))
  (cond ((equal name "l-hip-joint") (send *2d-model* :l-hip angle)))
  (cond ((equal name "l-knee") (send *2d-model* :l-knee angle)))
  )

(defun cb (msg)
  (setq name-list (send msg :joint_names))
  (setq angle-list (send (elt (send msg :points) 0) :positions))
  (print 2)
  (dotimes (i (length name-list)) (change-joint (elt name-list i) (elt angle-list i)))
  ; (dolist (joint joint-list) (change-joint joint))
  )

(ros::subscribe "/2d_human_joint" trajectory_msgs::JointTrajectory #'cb)

(setq *2d-model* (instance 2d-pose-model :init))
;;(objects *2d-model*)
(send *2d-model* :angle-vector #f(20 30 -20 -30 40 30 -40 -30))

(ros::rate 2)
(while (ros::ok)
  (objects (list *2d-model*))
  ;;(send *irtviewer* :draw-objects)
  (x::window-main-one)
  (print 1)
  ;;(ros::ros-info "")
  (ros::spin-once)
  (ros::sleep))
(exit)
