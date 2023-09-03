import cv2
import numpy as np
from matplotlib import pyplot as plt


cap=cv2.VideoCapture('vtest.avi')

ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    


