import cv2
import cv2.aruco as aruco
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opened")
    exit()

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejected = aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters
    )
    print("IDs:", ids)

    height, width = frame.shape[:2]

    # Faking calibration matrix 
    focal_length = width
    camera_matrix = np.array([[focal_length, 0, width/2],
                              [0, focal_length, height/2],
                              [0, 0, 1]], dtype=np.float32)

    dist_coeffs = np.zeros((5,1))

    if ids is not None:

        aruco.drawDetectedMarkers(frame, corners, ids)

        marker_length = 0.05  # 5cm demo value

        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(
            corners,
            marker_length,
            camera_matrix,
            dist_coeffs
        )

        for i in range(len(ids)):

            cv2.drawFrameAxes(
                frame,
                camera_matrix,
                dist_coeffs,
                rvecs[i],
                tvecs[i],
                0.03
            )

        # Adding  white space below frame for text
        extra_space = 80
        frame = cv2.copyMakeBorder(
            frame,
            0,
            extra_space,
            0,
            0,
            cv2.BORDER_CONSTANT,
            value=(255,255,255)
        )

        # Displaying IDs cleanly below image
        id_text = "Detected IDs: " + ", ".join(
            [str(id[0]) for id in ids]
        )

        cv2.putText(frame,
                    id_text,
                    (30, height + 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,0,0),
                    2)

    cv2.imshow("Live ArUco Detection", frame)

    key = cv2.waitKey(10) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
