import numpy as np
import cv2 as cv

def nothing(x):
    pass

#shade = np.zeros((200,150), dtype = np.uint8)

cv.namedWindow('Trackbars')
cv.resizeWindow('Trackbars', 512, 512)
cv.createTrackbar('color/gray', 'Trackbars', 0, 1, nothing)
cv.createTrackbar('Binary Thresh', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('Inverse Binary Thresh', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('Thresh Trunc', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('Thresh To 0', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('Thresh To 0 Inv', 'Trackbars', 0, 255, nothing)

while True:
    img = cv.imread('lena.png')

    pos = cv.getTrackbarPos('color/gray', 'Trackbars')
    th1_val = cv.getTrackbarPos('Binary Thresh', 'Trackbars')
    th2_val = cv.getTrackbarPos('Inverse Binary Thresh', 'Trackbars')
    th3_val = cv.getTrackbarPos('Thresh Trunc', 'Trackbars')
    th4_val = cv.getTrackbarPos('Thresh To 0', 'Trackbars')
    th5_val = cv.getTrackbarPos('Thresh To 0 Inv', 'Trackbars')
        
    #shade[:,:] = th1_val
    
    if pos == 1:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        pass

    _, th1 = cv.threshold(img, th1_val, 255, cv.THRESH_BINARY)
    _, th2 = cv.threshold(img, th2_val, 255, cv.THRESH_BINARY_INV)
    _, th3 = cv.threshold(img, th3_val, 255, cv.THRESH_TRUNC)
    _, th4 = cv.threshold(img, th4_val, 255, cv.THRESH_TOZERO)
    _, th5 = cv.threshold(img, th5_val, 255, cv.THRESH_TOZERO_INV)


    cv.imshow('Original Image', img)
    cv.imshow('Binary Thresholding', th1)
    cv.imshow('Inverse Binary Thresholding', th2)
    cv.imshow('Truncated Thresholding', th3)
    cv.imshow('Thresholding to Zero', th4)
    cv.imshow('Thresholding to Zero Inverse', th5)
    #cv.imshow('Shade', shade)

    
    if cv.waitKey(4) == 27:
        break


cv.destroyAllWindows()
