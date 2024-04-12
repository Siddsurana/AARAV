import cv2
import os
import face_recognition


distance_threshold = 0.5  


def load_known_face(folder_name):

    known_face_image = face_recognition.load_image_file(f"sample/{folder_name}/sample_{folder_name}.jpg")

    known_face_encoding = face_recognition.face_encodings(known_face_image)[0]
    return known_face_encoding


def detect_and_recognize_faces(frame, folder_name):

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


    known_face_encoding = load_known_face(folder_name)


    face_names = []


    for face_encoding in face_encodings:

        face_distance = face_recognition.face_distance([known_face_encoding], face_encoding)[0]


        if face_distance < distance_threshold:

            face_names.append(folder_name)
        else:
   
            face_names.append("Unknown")

    return face_locations, face_names


if __name__ == "__main__":

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  
    cam.set(4, 480)  

    
    folder_names = [name for name in os.listdir("sample") if os.path.isdir(os.path.join("sample", name))]

    while True:
        ret, frame = cam.read()

       
        for folder_name in folder_names:
            face_locations, face_names = detect_and_recognize_faces(frame, folder_name)

        
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

  
        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cam.release()
    cv2.destroyAllWindows()
