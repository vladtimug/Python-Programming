#This app will detect the contour of moving objects in a video stream from the webcam and display it on the stram

import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

ret1, frame1 = cap.read()
ret1, frame2 = cap.read()

def make_1920p():
    cap.set(3, 1920)
    cap.set(4, 720)                                    #change stream resolution to 1920p

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)                                     #change stream resolution to 720p

width  = cap.get(3) # 640
height = cap.get(4) # 480

print('Stream Res: ', width, ' x ', height)

while cap.isOpened():

    timer = cv2.getTickCount()
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    #cv2.putText(frame1, str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
    
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    #palms = palm_cascade.detectMultiScale(gray, 1.3, 5)

    #for x,y,w,h in hands:
    #    cv2.rectangle(frame2, (x,y), (x+w, y+h), (255, 0, 0), 2)
    #    roi_gray = gray [y: y+h, x: x+w]
    #    roi_color = frame2[y: y+h, x: x+w]

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)       #save coordinates of the found contours
        if cv2.contourArea(contour) < 8000:
            continue
        cv2.rectangle (frame1, (x,y), (x+w, y+h), (0,255,0), 2) #draw rectangle around the moving contours
        print(x,y,w,h)
        x_center = int(x+w/2)
        y_center = int(y+h/2)
        center_coords = (x_center, y_center)
        print (center_coords)
        frame1 = cv2.circle(frame1, center_coords, 3, (0, 255, 0), -1)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
   
    cv2.imshow('Stream', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    cv2.imshow('Thresh', thresh)
    cv2.imshow('Dilated', dilated)

    print('FPS: ', int(fps), end = '\r')
    #print('Data type: ', frame1.dtype)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()

#Mapping Function for a Cell bounding box of 225x242 mm 