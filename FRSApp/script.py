import face_recognition
import os

known_faces = []
known_names = []

def know_faces():
    image_folder = "D:/7th Semester/CV/Project/FRS/media/known_faces"

    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(filename.split(".")[0])

def identify(unknown_image):
    know_faces()
    unknown_image = face_recognition.load_image_file("D:/7th Semester/CV/Project/FRS/media/" + unknown_image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces(known_faces, unknown_encoding)
    for i, result in enumerate(results):
        if result:
            return (f"Face recognized as {known_names[i]}")
    return ("Face not recognized")