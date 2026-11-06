
# hill_climb_racing_gesture

## Overview

Real time Gesture Recognition system implemented using Python, OpenCV and MediaPipe. The application controls the game Hill Climb Racing by detecting hand gestures via webcam. Computer Vision and hand landmarks are used to detect gestures which are then mapped to keyboard presses using PyAutoGUI.

## Features

- Real-time hand tracking
- Gesture-based acceleration
- Gesture-based braking
- Webcam-controlled gameplay
- Low-latency response

## Technologies Used

| Technology |
|---|
| Python |
| OpenCV |
| MediaPipe |
| PyAutoGUI |

## Controls

| Gesture | Action |
|---|---|
| Palm | Accelerate |
| Fist | Brake |

## How It Works

1. Webcam captures hand movements.
2. MediaPipe detects body landmarks.
3. Hand position is tracked.
4. Gestures are mapped to keyboard inputs.
5. Hill Climb Racing responds instantly.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Project Structure

```text
hill-climbing-gesture-controller/
│
├── main.py
├── requirements.txt
├── README.md
```

## Author

Yash Srivastava

