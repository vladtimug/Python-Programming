#This application reads a video strem from the webcam and detects faces and face features using haar cascade algorithm.

import cv2
import numpy as np
import math

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)                               #get live video capture from device no 0 (main camera)

def make_1920p():
    cap.set(3, 1920)
    cap.set(4, 720)                                    #change stream resolution to 1920p

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)                                     #change stream resolution to 720p

if cap.isOpened() == False:
        print("Error accessing camera for live stream. Let me try again.")
        cap = cap.open(0)
else:
        print("Camera opened sucssesfully.")

def switch_col(x_val):               # return column containing center of detected face rectangle (== cases not approached yet)
    if x_val < 128:
        column = 1
        return column
    elif x_val > 128 and x_val < 256:
        column = 2
        return column
    elif x_val > 256 and x_val < 384:
        column = 3
        return column
    elif x_val > 384 and x_val < 512:
        column = 4
        return column
    elif x_val > 512 and x_val < 640:
        column = 5
        return column
    elif x_val == 128:
        column = 6
        return column
    elif x_val == 256:
        column = 7
        return column
    elif x_val == 384:
        column = 8
        return column
    elif x_val == 512:
        column = 9
        return column

def switch_row(y_val):                  # return row containing center of detected face rectangle (== cases not approached yet)
    if y_val < 160:
        row = 1
        return row
    elif y_val > 160 and y_val < 320:
        row = 2
        return row
    elif y_val > 320 and y_val < 480:
        row = 3
        return row
    elif y_val == 160:
        row = 4
        return row
    elif y_val == 320:
        row = 5
        return row

def grid_cell(row, col):                  # return cell containing center of detected face rectangle 
    if col == 1:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 6:
        for i in range (1, row + 1, 0.5):
            if row == i:
                cell = [row, col]
                break
    elif col == 2:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 7:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 3:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 8:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 4:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 9:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    elif col == 5:
        for i in range (1, row + 1):
            if row == i:
                cell = [row, col]
                break
    
    return cell

def active_cell (row, col):     #returns cell(s) to enable - current flag
    if  col == 1:
        for i in range (1, row+1):
            if row == 1:
                active_cell = 1
                return active_cell
            #elif row == 4:
            #    active_cell = [1, ]
            #    return active_cell
            #elif row == :
            #    active_cell = [1, 2]
            #    return active_cell
    #elif row == 1 and col == 2:
    #    active_cell = 2
    #    return active_cell
    #elif row == 1 and col == 3:
    #    active_cell = 2
    #    return active_cell

while True:
    ret, frame = cap.read()                                 #Create a videoCapture obj. Returns True or False depending on the status
    frame = cv2.flip(frame, 1)                              #Overcome mirroring effect
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #Apply grayscale filter to video stream
    
    #Draw Panel

    pts = np.array([[256,0], [192, 80], [192, 80], [128, 80], [64, 160], [0, 160], [0, 320], [64, 320], [128, 400], [192, 400], [256, 480], [384, 480], [448, 400],
                    [512, 400], [576, 320], [640, 320], [640, 160], [576, 160], [512, 80], [448, 80],  [384, 0], [256, 0]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(frame, [pts], True, (0, 255, 255), 2)
    frame = cv2.circle(frame, (int(640/2), int(480/2)), 3, (0, 255,255), -1)            # frame origin
    frame = cv2.line(frame, (128,0), (128, 480), (0, 255, 255), 2)
    frame = cv2.line(frame, (256,0), (256, 480), (0, 255, 255), 2)
    frame = cv2.line(frame, (384,0), (384, 480), (0, 255, 255), 2)
    frame = cv2.line(frame, (512,0), (512, 480), (0, 255, 255), 2)                      # panel columns
    frame = cv2.line(frame, (0, 160), (640, 160), (0, 255, 255), 2)
    frame = cv2.line(frame, (0, 320), (640, 320), (0, 255, 255), 2)                     # panel rows
    frame = cv2.line(frame, (128, 240), (256, 240), (0, 255, 255), 2)
    frame = cv2.line(frame, (384, 240), (512, 240), (0, 255, 255), 2)                   # devide cells on columns 2 and 4
    
    #Detect Faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        #roi_gray = gray [y: y+h, x:x+w]
        #roi_color = frame [y: y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)                   
        #for ex, ey, ew, eh in eyes:
        #    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        x_center = int(x+w/2)
        y_center = int(y+h/2)
        center_coords = (x_center, y_center)
        frame = cv2.circle(frame, center_coords, 3, (0, 255, 0), -1)
        #print (center_coords)

        # compute X coord of the face center wrt to frame origin
        x_face = int (x_center - 640/2)
        y_face = int (y_center - 420/2)
        #print ('Face at: ',  grid_cell(switch_row(y_center), switch_col(x_center)))


        #compute distance of face from camera
        depth = 0.0033 * h - 1.9918 * h + 372.83                #relationship between height of the face (in pixels) and the straight line from the camera to the object
        ratio = 0.0004 * depth - 0.1469 * depth + 18.119        #ratio between the object depth and the lateral physical distance to lateral pixel distance ratio from de camera center
        distance = math.sqrt(depth**2 + ratio **2)              #physical distance from the face to the camera
        if distance < 80:
            print (distance)


    window_name = 'Live Stream'
    cv2.imshow(window_name, frame)                              #Display colored camera live stream

    window_name2 = 'Live Stream Gray'                   
    cv2.imshow(window_name2, gray)                      #Display grayscale camera live stream

    if cv2.waitKey(1) & 0xFF == 27:               #Wait for 1 miliseconds and check for a key press event of x key to shut down live stream
        break

cap.release()
cv2.destroyAllWindows()
