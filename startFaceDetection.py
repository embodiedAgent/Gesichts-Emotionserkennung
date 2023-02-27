import cv2
from deepface import DeepFace

# source for selecting a camera, on sims-01 there are 3 cameras:
# 0: Azure Kinect 4K (right in front of you from the 180 degree screen)
# 1: Azure Kinect 4K (Middle in front of you from the 180 degree screen)
# 2: Azure Kinect Depth Camera
DeepFace.stream(db_path = "database", time_threshold=10, source = 1)