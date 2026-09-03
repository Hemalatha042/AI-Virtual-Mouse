import math

def distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def is_pinch(hand):
    return distance(hand.landmark[4], hand.landmark[8]) < 0.05

def is_two_fingers_up(hand):
    return (
        hand.landmark[8].y < hand.landmark[6].y and
        hand.landmark[12].y < hand.landmark[10].y and
        hand.landmark[16].y > hand.landmark[14].y
    )

def is_open_palm(hand):
    wrist = hand.landmark[0]
    tips = [4, 8, 12, 16, 20]
    return all(distance(wrist, hand.landmark[t]) > 0.3 for t in tips)

def is_thumb_up(hand):
    thumb = hand.landmark[4]
    thumb_ip = hand.landmark[3]

    index = hand.landmark[8]
    middle = hand.landmark[12]
    ring = hand.landmark[16]
    pinky = hand.landmark[20]

    thumb_up = thumb.y < thumb_ip.y
    fingers_down = (
        index.y > hand.landmark[6].y and
        middle.y > hand.landmark[10].y and
        ring.y > hand.landmark[14].y and
        pinky.y > hand.landmark[18].y
    )

    return thumb_up and fingers_down
