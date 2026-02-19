import cv2


image = cv2.imread("test_img-2.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Converting BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining yellow color range
lower_yellow = (15, 60, 60)
upper_yellow = (45, 255, 255)

# Creating mask
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Removing noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Finding  contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Drawing bounding boxes
for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Showing results
cv2.imshow("Detected Infected Leaves", image)
cv2.imshow("Yellow Mask", mask)

cv2.imwrite("output_detected_image-2.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


