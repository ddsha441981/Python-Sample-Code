# Author: Deendayal Kumawat
""" Date: 03/01/21
Descriptions: Security Camera Module With OpenCv In Python"""
import cv2

cam = cv2.VideoCapture(0)
while cam.isOpened():
    # Variables
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    differance = cv2.absdiff(frame1,frame2)

    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("ddsha's Security Camera", differance)
