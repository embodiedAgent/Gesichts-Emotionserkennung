import cv2
from deepface import DeepFace


DeepFace.stream(db_path = "database", time_threshold=10)