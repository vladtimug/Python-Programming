import cv2 as cv

def nothing(x):
    pass
img = cv.imread('sudoku.jpg', 0)

cv.namedWindow('Trackbars')

cv.createTrackbar('Th1_BlockSize', 'Trackbars', 0, 100, nothing)
cv.createTrackbar('Const_1', 'Trackbars', 0, 50, nothing)
cv.createTrackbar('Th2_BlockSize', 'Trackbars', 0, 100, nothing)
cv.createTrackbar('Const_2', 'Trackbars', 0, 50, nothing)

while True:

    th1_val = cv.getTrackbarPos('Th1_BlockSize', 'Trackbars')
    if th1_val % 2 == 0 and th1_val > 3:
        th1_val -= 1
    elif th1_val in range(3):
        th1_val = 3

    th2_val = cv.getTrackbarPos('Th2_BlockSize', 'Trackbars')
    if th2_val % 2 == 0 and th2_val > 3:
        th2_val -= 1
    elif th2_val in range(3):
        th2_val = 3
    c1_val = cv.getTrackbarPos('Const_1', 'Trackbars')
    c2_val = cv.getTrackbarPos('Const_2', 'Trackbars')
    
    th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                  cv.THRESH_BINARY, th1_val, c1_val)

    th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv.THRESH_BINARY, th2_val, c2_val)

    cv.imshow('Initial Image', img)

    cv.imshow('Mean', th1)
    cv.imshow('Gaussian', th2)

    if cv.waitKey(2) == 27:
        break

cv.destroyAllWindows()
