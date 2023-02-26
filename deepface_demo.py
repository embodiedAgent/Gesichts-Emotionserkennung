from deepface import DeepFace

# using images demo
result = DeepFace.verify(img1_path = "./database/image1.jpg", img2_path = "./database/image2.jpg")

print(result)

# real time demo
DeepFace.stream(db_path = "./database")