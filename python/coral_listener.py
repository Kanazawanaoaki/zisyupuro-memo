#!/usr/bin/env python

import rospy
from jsk_recognition_msgs.msg import PeoplePose
from jsk_recognition_msgs.msg import PeoplePoseArray

point_list = []

def cb(msg):
    try:
        limb_list = msg.poses[0].limb_names
        print len(msg.poses[0].limb_names)
        print msg.poses[0].limb_names[0]
        print msg.poses[0].poses[0]
    except:
        print "no massage!"

rospy.init_node('coral_listener')
rospy.Subscriber('/edgetpu_human_pose_estimator/output/poses',PeoplePoseArray,cb)
# pub = rospy.Publisher('/2d_human_joint',)
rospy.spin()
