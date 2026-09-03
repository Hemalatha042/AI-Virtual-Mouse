# AI-Virtual-Mouse
AI-powered virtual mouse using hand gesture recognition and computer vision.
# AI Virtual Mouse Using Hand Gesture Recognition

## 📌 Project Overview

The **AI Virtual Mouse** is a touchless computer mouse control system that allows users to control the mouse cursor using hand gestures. The system uses a webcam to capture real-time hand movements and computer vision techniques to detect and recognize gestures.

MediaPipe is used to detect hand landmarks, while PyAutoGUI performs mouse actions such as cursor movement, left click, right click, and drag.

## ✨ Features

* Real-time hand tracking using a webcam
* Touchless cursor movement
* Left click using pinch gesture
* Right click using two-finger gesture
* Drag operation using fist gesture
* Cursor smoothing to reduce shaking
* Real-time gesture display
* No additional hardware required

## 🖐️ Gesture Controls

| Hand Gesture             | Mouse Action     |
| ------------------------ | ---------------- |
| ☝️ Index finger movement | Move cursor      |
| 🤏 Pinch (Index + Thumb) | Left click       |
| ✌️ Two fingers up        | Right click      |
| ✊ Fist                   | Drag             |
| ⎋ ESC key                | Exit application |

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – Webcam and image processing
* **MediaPipe** – Hand landmark detection
* **PyAutoGUI** – Mouse control
* **ScreenInfo** – Screen resolution detection

## 📂 Project Structure

```text
AI_Virtual_Mouse_Project/
│
├── app.py
├── gesture_utils.py
├── hand_test.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ How to Run

Connect your webcam and run:

```bash
python app.py
```

The webcam window will open and detect your hand.

Use the supported hand gestures to control the mouse.

Press **ESC** to stop the application.

## 🧠 How It Works

1. The webcam captures live video frames.
2. OpenCV processes the captured frames.
3. MediaPipe detects the hand and identifies **21 hand landmarks**.
4. The index-finger coordinates are mapped to the computer screen.
5. PyAutoGUI moves the mouse cursor according to the hand movement.
6. Gesture recognition logic identifies gestures such as pinch, two fingers, and fist.
7. The corresponding mouse action is performed.

## 🎯 Applications

* Touchless computer interaction
* Accessibility systems
* Smart kiosks
* Presentation control
* Healthcare environments
* Human-Computer Interaction (HCI)
* Educational projects

## 🚀 Future Enhancements

* Add more hand gestures
* Improve gesture recognition accuracy
* Add customizable gestures
* Add voice commands
* Improve cursor smoothing
* Develop a graphical settings interface
* Optimize the system for touchless healthcare applications

## 👩‍💻 Author

**Hemalatha P**

MCA Student | AI/ML & Python Enthusiast

## 📜 License

This project is created for educational and project demonstration purposes.
