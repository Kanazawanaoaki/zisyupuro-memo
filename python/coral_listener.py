#!/usr/bin/env python

import numpy as np
import rospy
from jsk_recognition_msgs.msg import PeoplePose
from jsk_recognition_msgs.msg import PeoplePoseArray

# referencail list of using limb namse
ref_list = ["left shoulder","right shoulder","left elbow","right elbow","left wrist","right wrist","left hip","right hip","left knee","right knee","left ankle","right ankle"]

# Threshold of scores
score_thre = 0.8

def cb(msg):
    try:
        # dfine dictionary of flag,x position,and y position
        flag_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}
        xpos_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}
        ypos_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}
        score_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}

        # make list of limb'name from ROS message
        limb_list = msg.poses[0].limb_names

        # get positions of limbs
        for i in range(len(limb_list)):
            if limb_list[i] in ref_list and msg.poses[0].scores[i] > score_thre:
                # print limb_list[i]
                flag_dict[limb_list[i]] = 1
                xpos_dict[limb_list[i]] = msg.poses[0].poses[i].position.x
                ypos_dict[limb_list[i]] = msg.poses[0].poses[i].position.y

        # calc jointangle ['r-shoulder','r-elbow','l-shoulder','l-elbow','r-hip-joint','r-knee','l-hip-joint','l-knee']
        if flag_dict["right shoulder"] == 1 and flag_dict["left shoulder"] == 1 and flag_dict["right elbow"]:
            print "able to calculate angle of r-shoulder !"


        print len(msg.poses[0].limb_names)
        print msg.poses[0].limb_names[0]
        print msg.poses[0].poses[0]
        print msg.poses[0].scores[0]
        print flag_dict[msg.poses[0].limb_names[5]]
    except:
        print "no massage!"

rospy.init_node('coral_listener')
rospy.Subscriber('/edgetpu_human_pose_estimator/output/poses',PeoplePoseArray,cb)
# pub = rospy.Publisher('/2d_human_joint',)
rospy.spin()
