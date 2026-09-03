import cv2
import time
import pyautogui
from screeninfo import get_monitors
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from gesture_utils import (
    is_pinch,
    is_two_fingers_up,
    is_open_palm,
    is_thumb_up
)

# ================= CONFIG =================
pyautogui.FAILSAFE = False
CLICK_DELAY = 0.7
DRAG_HOLD_TIME = 0.4
SMOOTHING = 7
# ==========================================

monitor = get_monitors()[0]
SCREEN_W, SCREEN_H = monitor.width, monitor.height

cap = cv2.VideoCapture(0)
hands = Hands(max_num_hands=1)

prev_x, prev_y = 0, 0
last_click_time = 0

drag_active = False
thumb_start_time = None
open_palm_start = None

print("AI Virtual Mouse Started")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        draw_landmarks(frame, hand, HAND_CONNECTIONS)

        # -------- CURSOR MOVE (INDEX FINGER) --------
        idx = hand.landmark[8]
        x = int(idx.x * SCREEN_W)
        y = int(idx.y * SCREEN_H)

        curr_x = prev_x + (x - prev_x) / SMOOTHING
        curr_y = prev_y + (y - prev_y) / SMOOTHING

        pyautogui.moveTo(curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y

        # -------- LEFT CLICK (☝️ PINCH) --------
        if is_pinch(hand):
            if time.time() - last_click_time > CLICK_DELAY:
                pyautogui.click()
                last_click_time = time.time()
                print("LEFT CLICK")

        # -------- RIGHT CLICK (✌️) --------
        elif is_two_fingers_up(hand):
            if time.time() - last_click_time > CLICK_DELAY:
                pyautogui.rightClick()
                last_click_time = time.time()
                print("RIGHT CLICK")

        # -------- DRAG (👍 HOLD) --------
        if is_thumb_up(hand):
            if thumb_start_time is None:
                thumb_start_time = time.time()

            elif time.time() - thumb_start_time > DRAG_HOLD_TIME:
                if not drag_active:
                    pyautogui.mouseDown()
                    drag_active = True
                    print("DRAG START")

        else:
            thumb_start_time = None
            if drag_active:
                pyautogui.mouseUp()
                drag_active = False
                print("DRAG STOP")

        # -------- EXIT (✋ HOLD 2s) --------
        if is_open_palm(hand):
            if open_palm_start is None:
                open_palm_start = time.time()
            elif time.time() - open_palm_start > 2:
                print("EXIT")
                break
        else:
            open_palm_start = None

    cv2.imshow("AI Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
hands.close()
cv2.destroyAllWindows()
