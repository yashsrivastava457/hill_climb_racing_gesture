# hill_climb_racing_gesture

Overview
Real time Gesture Recognition system implemented using Python, OpenCV and MediaPipe. The application controls the game Hill Climb Racing by detecting hand gestures via webcam. Computer Vision and hand landmarks are used to detect gestures which are then mapped to keyboard presses using PyAutoGUI.

Features
Real-time hand tracking
Gesture-based acceleration
Gesture-based braking
Webcam-controlled gameplay
Low-latency response

Technologies Used
Python
Opencv
Mediapipe
pyautogui

Controls
Gesture	Action
Palm	Accelerate
Fist	Brake
How It Works
Webcam captures hand movements.
MediaPipe detects body landmarks.
Hand position is tracked.
Gestures are mapped to keyboard inputs.
Hill Climb Racing responds instantly.

Installation
pip install -r requirements.txt
Run
python main.py
Project Structure
hill-climbing-gesture-controller/
│
├── main.py
├── requirements.txt
├── README.md

Author
Yash Srivastava
