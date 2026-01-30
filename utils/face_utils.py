# utils/face_utils.py

import dlib
import cv2
from imutils import face_utils

# Load models once (efficient)
detector = dlib.get_frontal_face_detector()

def load_landmark_predictor(model_path):
    return dlib.shape_predictor(model_path)

def get_faces(gray_frame):
    return detector(gray_frame, 0)

def get_eye_landmarks(gray_frame, face, predictor):
    shape = predictor(gray_frame, face)
    shape = face_utils.shape_to_np(shape)

    left_eye = shape[36:42]
    right_eye = shape[42:48]

    return left_eye, right_eye
