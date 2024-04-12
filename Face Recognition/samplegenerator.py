import cv2
import os


sample_folder = "sample"
if not os.path.exists(sample_folder):
    os.makedirs(sample_folder)


def capture_samples(person_id):
    
    person_folder = os.path.join(sample_folder, str(person_id))
    if not os.path.exists(person_folder):
        os.makedirs(person_folder)

    
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  
    cam.set(4, 480)  

    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    
    sample_count = 0
    while True:
        ret, frame = cam.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sample_count += 1

            
            sample_path = os.path.join(person_folder, f"sample_{sample_count}.jpg")
            cv2.imwrite(sample_path, frame[y:y + h, x:x + w])

        cv2.imshow('Capturing Samples', frame)
        k = cv2.waitKey(100) & 0xff
        if k == 27:  
            break
        elif sample_count >= 10:  
            break

    
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    
    person_id = input("Enter your ID: ")


    capture_samples(person_id)

    print("Samples captured successfully.")
