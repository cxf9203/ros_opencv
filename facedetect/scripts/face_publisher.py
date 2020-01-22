#!/usr/bin/env python

import numpy as np
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge



def face_publisher():
    rospy.init_node('face_publisher', anonymous=True)
    face_pub = rospy.Publisher('/image', Image, queue_size=1)
    face_cascade = cv2.CascadeClassifier('/home/cxf/opencv/data/haarcascades/haarcascade_frontalface_default.xml')// include your opencv haarcascade_frontalface_default.xml repository
    

    path = '/home/cxf/catkin_ws/src/facedetect/scripts'
    
    eye_cascade = cv2.CascadeClassifier('/home/cxf/opencv/data/haarcascades/haarcascade_eye.xml')// include your opencv haarcascade_frontalface_default.xml repository
    
    rate = rospy.Rate(10)
    cap = cv2.VideoCapture(0)
    bridge = CvBridge()
    
    while not rospy.is_shutdown():
       ret, frame = cap.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       faces = face_cascade.detectMultiScale(gray, 1.3, 5)
       for (x, y, w, h) in faces:

          frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
          roi_gray = gray[y:y + h, x:x + w]
          roi_color = frame[y:y + h, x:x + w]
          eyes = eye_cascade.detectMultiScale(roi_gray)

          for (ex, ey, ew, eh) in eyes:
              cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
       
       msg = bridge.cv2_to_imgmsg(frame, "bgr8")
       face_pub.publish(msg)
       print '** publishing face_frame ***'
       rate.sleep()
        


if __name__ == '__main__':
    try:
        face_publisher()
    except rospy.ROSInterruptException:
        pass

