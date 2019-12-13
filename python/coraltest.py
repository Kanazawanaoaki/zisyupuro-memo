#!/usr/bin/env python

import numpy as np
import rospy
from jsk_recognition_msgs.msg import PeoplePose
from jsk_recognition_msgs.msg import PeoplePoseArray

flag_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0}

def cb(msg):
    try:
        limb_list = msg.poses[0].limb_names
        print len(msg.poses[0].limb_names)
        print msg.poses[0].limb_names[0]
        print msg.poses[0].poses[0]
        print flag_dict[msg.poses[0].limb_names[5]]
        flag_dict[msg.poses[0].limb_names[5]] += 1
    except:
        print "no massage!"

rospy.init_node('coral_listener')
rospy.Subscriber('/edgetpu_human_pose_estimator/output/poses',PeoplePoseArray,cb)
# pub = rospy.Publisher('/2d_human_joint',)
rospy.spin()
