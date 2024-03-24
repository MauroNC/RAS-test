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
        # Capturar o frame da câmera
        ret, frame = cap.read()

        if not ret:
            print("Falha ao capturar o frame da câmera. Certifique-se de que a webcam esteja conectada e tente executar o código novamente.")
            break

        # Converta o frame para o formato RGB e processe-o com o modelo de mãos do MediaPipe
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detecte mãos no quadro
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            # Inicialize o número total de dedos levantados
            total_fingers_up = 0

            # Contar o número de dedos para cada mão
            for hand_landmarks in results.multi_hand_landmarks:
                # Obtenha as coordenadas dos pontos de referência dos dedos
                finger_landmarks = {
                    'thumb': hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP],
                    'index': hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                    'middle': hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                    'ring': hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                    'pinky': hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
                }

                # Contar o número de dedos levantados
                num_fingers_up_hand = sum(1 for landmark in finger_landmarks.values() if landmark.y < 0.5)
                total_fingers_up += num_fingers_up_hand

            # Exiba o número total de dedos levantados
            frame = cv2.putText(frame, f'{total_fingers_up} dedos levantados', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                                2)

            # Desenhe os pontos de referência das mãos
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        else:
            frame = cv2.putText(frame, "Aproxime as maos para a camera", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                                2)

        # Exiba o frame em uma janela
        cv2.imshow('Hand Tracking', frame)

        # Interromper o loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar a câmera
if cap.isOpened():
    cap.release()

# Fechar as janelas do OpenCV
cv2.destroyAllWindows