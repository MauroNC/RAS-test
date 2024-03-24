import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize the camera
if not cv2.VideoCapture(0).isOpened():
    print("Camera is not available. Make sure the webcam is connected and try running the code again.")
    exit()

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6) as hands:

    while True:
        # Capture the frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture the frame from the camera. Make sure the webcam is connected and try running the code again.")
            break

        # Convert the frame to RGB format and process it with the MediaPipe hands model
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            # Initialize the total number of fingers raised
            total_fingers_up = 0

            # Count the number of fingers for each hand
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the coordinates of the finger landmarks
                finger_landmarks = {
                    'thumb': hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP],
                    'index': hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                    'middle': hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                    'ring': hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                    'pinky': hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
                }

                # Count the number of fingers raised
                num_fingers_up_hand = sum(1 for landmark in finger_landmarks.values() if landmark.y < 0.5)
                total_fingers_up += num_fingers_up_hand

            # Display the total number of fingers raised
            frame = cv2.putText(frame, f'{total_fingers_up} dedos levantados', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                                2)

            # Draw the hand landmarks
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        else:
            frame = cv2.putText(frame, "Aproxime as maos para a camera", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                                2)

        # Show the frame in a window
        cv2.imshow('Hand Tracking', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera
if cap.isOpened():
    cap.release()

# Close the OpenCV windows
cv2.destroyAllWindows