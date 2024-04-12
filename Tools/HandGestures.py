import cv2
import mediapipe as mp
import pyautogui

# Set up screen dimensions
screen_width, screen_height = pyautogui.size()

# Set up MediaPipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Set up camera
cap = cv2.VideoCapture(0)

# Variable to track scrolling direction
scroll_direction = None
scroll_speed = 30

def start_hand_gesture_recognition():
    global cap
    cap = cv2.VideoCapture(0)

def stop_hand_gesture_recognition():
    global cap
    cap.release()
    cv2.destroyAllWindows()

def perform_scroll(direction):
    global scroll_speed
    if direction == 'up':
        pyautogui.scroll(scroll_speed)
    elif direction == 'down':
        pyautogui.scroll(-scroll_speed)

if __name__ == "__main__":
    while cap.isOpened():
        # Read frame from camera
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Hands
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            # Get the landmarks of the first hand
            hand_landmarks = results.multi_hand_landmarks[0]

            # Get thumb and index finger landmarks
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            # Check if thumb is up and other fingers are down
            if thumb_tip.y < index_finger_tip.y and thumb_tip.y < middle_finger_tip.y and \
               thumb_tip.y < ring_finger_tip.y and thumb_tip.y < pinky_tip.y:
                # Scroll up
                perform_scroll('up')
                scroll_direction = 'up'

            # Check if thumb is down and other fingers are up
            elif thumb_tip.y > index_finger_tip.y and thumb_tip.y > middle_finger_tip.y and \
                 thumb_tip.y > ring_finger_tip.y and thumb_tip.y > pinky_tip.y:
                # Scroll down
                perform_scroll('down')
                scroll_direction = 'down'
            else:
                scroll_direction = None

        else:
            # No hand detected, stop scrolling
            scroll_direction = None

        # Display the frame


        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
