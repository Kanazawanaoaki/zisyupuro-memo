#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import UInt8

ref_list = ["r-shoulder","r-elbow","l-shoulder","l-elbow","r-hip-joint","r-knee","l-hip-joint","l-knee"]

max_angle = 179
min_angle = 1

array = [145,135,35,45,160,110,20,70]

def adj_val(val):
    val = int(round(val)) + 90
    if val > max_angle:
        val = max_angle
    if val < min_angle:
        val = min_angle
    return val

def cb(msg):
    try:
        # print "hey"
        name_list = msg.joint_names
        angle_list = msg.points[0].positions

        ind = 0

        for i in range(8):
            if ref_list[i] in name_list:
                array[i] = adj_val(angle_list[ind])
                # print adj_val(angle_list[ind])
                ind += 1

        print msg.joint_names
        print array

        num_array = UInt8MultiArray()
        num_array.data = array
        pub.publish(num_array)

    except:
        print "no massage!"


print "start"
rospy.init_node('pose_unint')
rospy.Subscriber('/2d_human_joint',JointTrajectory,cb)
pub = rospy.Publisher('/arduino_angle',UInt8MultiArray,queue_size=1)
rospy.sleep(1)
rospy.spin()
