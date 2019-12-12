#!/usr/bin/env python

import math
import rospy
import sys
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

import cv2

# point_list = []

def send_joint_position():
    try:
        # while True:
            print(1)
            rospy.init_node('send_joint_position')
            pub = rospy.Publisher('/2d_human_joint',JointTrajectory,queue_size=1)
            rospy.sleep(1)

            for i in range(100):
                joint_trajectory = JointTrajectory()
                joint_trajectory.header.stamp = rospy.Time.now()
                joint_trajectory.joint_names = ['r-shoulder','r-elbow','l-shoulder','l-elbow','r-hip-joint','r-knee','l-hip-joint','l-knee']

                point = JointTrajectoryPoint()
                point.positions = [-60+i,-20+i,-50+i,-30+i,40,20,40,30]#point_list
                joint_trajectory.points.append(point)
                pub.publish(joint_trajectory)
                rospy.sleep(1)
                if cv2.waitKey(0) == 27:
                    print("finish")
                    break
    except  KeyboardInterrupt:
        print('!!FINISH!!')
        sys.exit(0)

if __name__ == '__main__':
    try:
        send_joint_position()
    except rospy.ROSInterruptException: pass
