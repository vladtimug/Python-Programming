import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    ret = 0
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray, 1)
        edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
        color = cv.bilateralFilter(frame, 9, 250, 250)
        cartoon = cv.bitwise_and(color, color, mask=edges)
        # cv.imshow("rgbFrame", frame)
        # cv.imshow("cartoon", cartoon)
        # cv.imshow("color", color)
        cv.imshow("edges", edges)
        if cv.waitKey(1) == 27:
            break
    else:
        print("Error occured. Frame grabbing failed.")
        break

cap.release()
cv.destroyAllWindows()
