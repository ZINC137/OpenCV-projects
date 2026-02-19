import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

# Checking if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width = frame.shape[:2]

    cx = width // 2
    cy = height // 2

    cv2.circle(frame, (cx, cy), 5, (0,0,255), 2)

    pixel_value = hsv_frame[cy, cx]
    hue_value = pixel_value[0]

    if 18 <= hue_value <= 40:
        color_name = "Yellow"
    else:        color_name = "Not Yellow"

    text = f"HSV: {pixel_value}, Color: {color_name}"
    cv2.putText(frame, text, (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (75, 50, 255), 2)

    cv2.imshow("Live Detection", frame)

    key = cv2.waitKey(10) & 0xFF

    if key == 27 or key == ord('q'):  # ESC
        print("ESC pressed")
        print("Key value:", key)
        break
cap.release()
cv2.destroyAllWindows()