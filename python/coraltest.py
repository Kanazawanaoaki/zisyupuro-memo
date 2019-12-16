#!/usr/bin/env python

import numpy as np
import math
import rospy
from jsk_recognition_msgs.msg import PeoplePose
from jsk_recognition_msgs.msg import PeoplePoseArray
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

# referencail list of using limb namse
ref_list = ["left shoulder","right shoulder","left elbow","right elbow","left wrist","right wrist","left hip","right hip","left knee","right knee","left ankle","right ankle"]

def calc_angle(x0,y0,x1,y1,x2,y2):

    A = np.array([x1-x0,y1-y0])
    B = np.array([x2-x0,y2-y0])

    A3 = np.array([x1-x0,y1-y0,0])
    B3 = np.array([x2-x0,y2-y0,0])

    cross = np.cross(A3,B3)
    # print(cross[2])

    s = np.linalg.norm(A)
    t = np.linalg.norm(B)

    x = np.inner(A,B)
    # print(x)

    theta = np.arccos(x/(s*t))
    # print(theta)

    deg = 180 - math.degrees(theta)
    # print(deg)

    if cross[2] < 0:
        deg *= -1


    return deg


def cb(msg):
    try:
        # dfine dictionary of flag,x position,and y position
        flag_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}
        xpos_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}
        ypos_dict = {"left shoulder":0,"right shoulder":0,"left elbow":0,"right elbow":0,"left wrist":0,"right wrist":0,"left hip":0,"right hip":0,"left knee":0,"right knee":0,"left ankle":0,"right ankle":0}

        # make list of limb'name from ROS message
        limb_list = msg.poses[0].limb_names

        # make objects for ROS
        joint_trajectory = JointTrajectory()
        joint_trajectory.header.stamp = rospy.Time.now()
        name_list = []
        angle_list = []

        point = JointTrajectoryPoint()

        # get positions of limbs
        for i in range(len(limb_list)):
            if limb_list[i] in ref_list:
                # print limb_list[i]
                flag_dict[limb_list[i]] = 1
                xpos_dict[limb_list[i]] = msg.poses[0].poses[i].position.x
                ypos_dict[limb_list[i]] = msg.poses[0].poses[i].position.y

        # calc jointangle ['r-shoulder','r-elbow','l-shoulder','l-elbow','r-hip-joint','r-knee','l-hip-joint','l-knee']
        # r-shoulder
        if flag_dict["right shoulder"] == 1 and flag_dict["left shoulder"] == 1 and flag_dict["right elbow"]:
            print "able to calculate angle of r-shoulder !"
            r_shoulder = calc_angle(xpos_dict["right shoulder"],ypos_dict["right shoulder"],xpos_dict["left shoulder"],ypos_dict["left shoulder"],xpos_dict["right elbow"],ypos_dict["right elbow"])
            print "r-shoulder joint nalge = {0}".format(r_shoulder)
            name_list.append("r-shoulder")
            angle_list.append(r_shoulder)

        # r-elbow
        if flag_dict["right elbow"] == 1 and flag_dict["right shoulder"] == 1 and flag_dict["right wrist"]:
            print "able to calculate angle of r-elbow !"
            r_elbow = calc_angle(xpos_dict["right elbow"],ypos_dict["right elbow"],xpos_dict["right shoulder"],ypos_dict["right shoulder"],xpos_dict["right wrist"],ypos_dict["right wrist"])
            print "r-elbow joint nalge = {0}".format(r_elbow)
            name_list.append("r-elbow")
            angle_list.append(r_elbow)

        # l-shoulder
        if flag_dict["left shoulder"] == 1 and flag_dict["right shoulder"] == 1 and flag_dict["left elbow"]:
            print "able to calculate angle of l-shoulder !"
            l_shoulder = calc_angle(xpos_dict["left shoulder"],ypos_dict["left shoulder"],xpos_dict["right shoulder"],ypos_dict["right shoulder"],xpos_dict["left elbow"],ypos_dict["left elbow"])
            print "l-shoulder joint nalge = {0}".format(l_shoulder)
            name_list.append("l-shoulder")
            angle_list.append(l_shoulder)

        # l-elbow
        if flag_dict["left elbow"] == 1 and flag_dict["left shoulder"] == 1 and flag_dict["left wrist"]:
            print "able to calculate angle of l-elbow !"
            l_elbow = calc_angle(xpos_dict["left elbow"],ypos_dict["left elbow"],xpos_dict["left shoulder"],ypos_dict["left shoulder"],xpos_dict["left wrist"],ypos_dict["left wrist"])
            print "l-elbow joint nalge = {0}".format(l_elbow)
            name_list.append("l-elbow")
            angle_list.append(l_elbow)

        # r-hip-joint
        if flag_dict["right hip"] == 1 and flag_dict["left hip"] == 1 and flag_dict["right knee"]:
            print "able to calculate angle of r-hip-joint !"
            r_hip_joint = calc_angle(xpos_dict["right hip"],ypos_dict["right hip"],xpos_dict["left hip"],ypos_dict["left hip"],xpos_dict["right knee"],ypos_dict["right knee"])
            print "r-hip-joint joint nalge = {0}".format(r_hip_joint)
            name_list.append("r-hip-joint")
            angle_list.append(r_hip_joint)

        # r-knee
        if flag_dict["right knee"] == 1 and flag_dict["right hip"] == 1 and flag_dict["right ankle"]:
            print "able to calculate angle of r-knee !"
            r_knee = calc_angle(xpos_dict["right knee"],ypos_dict["right knee"],xpos_dict["right hip"],ypos_dict["right hip"],xpos_dict["right ankle"],ypos_dict["right ankle"])
            print "r-knee joint nalge = {0}".format(r_knee)
            name_list.append("r-knee")
            angle_list.append(r_knee)

        # l-hip-joint
        if flag_dict["left hip"] == 1 and flag_dict["right hip"] == 1 and flag_dict["left knee"]:
            print "able to calculate angle of l-hip-joint !"
            l_hip_joint = calc_angle(xpos_dict["left hip"],ypos_dict["left hip"],xpos_dict["right hip"],ypos_dict["right hip"],xpos_dict["left knee"],ypos_dict["left knee"])
            print "l-hip-joint joint nalge = {0}".format(l_hip_joint)
            name_list.append("l-hip-joint")
            angle_list.append(l_hip_joint)

        # l-knee
        if flag_dict["left knee"] == 1 and flag_dict["left hip"] == 1 and flag_dict["left ankle"]:
            print "able to calculate angle of l-knee !"
            l_knee = calc_angle(xpos_dict["left knee"],ypos_dict["left knee"],xpos_dict["left hip"],ypos_dict["left hip"],xpos_dict["left ankle"],ypos_dict["left ankle"])
            print "l-knee joint nalge = {0}".format(l_knee)
            name_list.append("l-knee")
            angle_list.append(l_knee)

        # publish ROS message
        joint_trajectory.joint_names = name_list

        point.positions = angle_list
        joint_trajectory.points.append(point)
        pub.publish(joint_trajectory)
        rospy.sleep(1)


    except:
        print "no massage!"

rospy.init_node('coral_listener')
rospy.Subscriber('/edgetpu_human_pose_estimator/output/poses',PeoplePoseArray,cb)
pub = rospy.Publisher('/2d_human_joint',JointTrajectory,queue_size=1)
rospy.sleep(1)
rospy.spin()
