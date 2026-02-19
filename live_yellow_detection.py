import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Defining yellow color range in HSV
    lower_yellow = np.array([18, 70, 80])
    upper_yellow = np.array([45, 255, 255])

   
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                  cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 200:   
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x,y), (x+w, y+h),
                          (0,0,255), 2)

    cv2.imshow("Plant Health Detection", frame)

    key = cv2.waitKey(10) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
