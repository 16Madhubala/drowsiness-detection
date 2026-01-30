import cv2
import mediapipe as mp
import numpy as np

from utils.eye_utils import eye_aspect_ratio, LEFT_EYE, RIGHT_EYE
from utils.alert_utils import play_alarm
from config import EAR_THRESHOLD, CONSEC_FRAMES, ALARM_PATH

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(max_num_faces=1)

cap = cv2.VideoCapture(0)
counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face in result.multi_face_landmarks:
            h, w, _ = frame.shape
            landmarks = np.array([
                [int(lm.x * w), int(lm.y * h)]
                for lm in face.landmark
            ])

            left_eye = landmarks[LEFT_EYE]
            right_eye = landmarks[RIGHT_EYE]

            ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2

            if ear < EAR_THRESHOLD:
                counter += 1
                if counter >= CONSEC_FRAMES:
                    cv2.putText(frame, "DROWSY!", (30, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                    play_alarm(ALARM_PATH)
            else:
                counter = 0

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
