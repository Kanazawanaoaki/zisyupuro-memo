#! /usr/bin/env roseus

(ros::roseus-add-msgs "jsk_recognition_msgs")

(ros::roseus "coral-listener" :anonymous t)

(defun cb (msg)
  )

(ros::subscribe "/edgetpu_human_pose_estimator/output/poses" jsk_recognition_msgs::PeoplePoseArray #'cb)

(ros::rate 10)
(while (ros::ok)
  ;;(ros::ros-info "")
  (ros::spin-once)
  (ros::sleep))
(exit)
