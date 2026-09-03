import cv2
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS

cap = cv2.VideoCapture(0)
hands = Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

print("Camera started. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera read failed")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw_landmarks(frame, handLms, HAND_CONNECTIONS)

    cv2.imshow("Hand Test", frame)

    if cv2.waitKey(10) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
print("Camera closed safely")
