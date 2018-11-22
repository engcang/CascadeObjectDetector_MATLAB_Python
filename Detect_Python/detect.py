#!/usr/bin/env python
"""
Created on Tue Nov  6 17:36:50 2018

@author: mason
"""

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)
detector_start = cv2.CascadeClassifier('start.xml')
detector_flower = cv2.CascadeClassifier('flowerpot.xml')
detector_experi = cv2.CascadeClassifier('experiment.xml')
detector_toilet = cv2.CascadeClassifier('toilet.xml')
detectors=[detector_start, detector_flower, detector_experi, detector_toilet]
Colors=[(0,0,255),(255,0,50),(30,30,30),(50,255,0)]
Texts=['start','flower','experi','toilet']
time.sleep(1)

def detecting(image):
    scale=1.2 # resize .*100%, smaller detect more but take longer
    minNeighbors=6 # higer, higer quality, less detection
    for i in range(0,4):
        detected_img = detectors[i].detectMultiScale(image,scale,minNeighbors)
        for (x,y,w,h) in detected_img:
            cv2.rectangle(image, (x,y), (x+w,y+h),Colors[i], 2)
            cv2.putText(image,Texts[i],(x-5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.3,Colors[i], 2)
while 1:
    a=time.time()
    ret, image = cap.read()
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detecting(image)
    print(time.time()-a)    
    cv2.imshow('detected_image',image)
    if cv2.waitKey(1)>0 : break
