#!/usr/bin/env python

import numpy as np
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge



def callback(data):
    global count,bridge
    count = count + 1
    if count == 1:
        count = 0
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("frame" , cv_img)
        cv2.waitKey(1)
    else:
        pass


def face_subscriber():
    rospy.init_node('face_subscriber', anonymous=True)
    global count,bridge
    count = 0
    bridge = CvBridge()
    rospy.Subscriber('/image', Image, callback)
    rospy.spin()
 
if __name__ == '__main__':
    face_subscriber()

