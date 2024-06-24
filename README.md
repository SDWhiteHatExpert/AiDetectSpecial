# AiDetectSpecial
# Virtual Mouse with Morse Code Translation

This project implements a virtual mouse using hand gestures detected through a webcam and translates Morse code gestures into text. It utilizes OpenCV for video processing, MediaPipe for hand tracking, and PyAutoGUI for simulating keyboard input. 

## Features

- **Virtual Mouse Control:** The index finger and thumb tips are tracked to control the mouse cursor.
- **Morse Code Translation:** Gestures are translated into Morse code and then into text, allowing for text input via hand signals.
- **Real-Time Processing:** The application processes the video feed in real-time, providing immediate feedback and interaction.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone the repository:
    ```sh
    git clone 
    cd virtual-mouse-morse-code
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

Run the main script to start the application:

```sh
python main.py
```

### Gestures for Morse Code

- **Dot (.)**: Quickly pinch your thumb and index finger together and release (less than 0.5 seconds).
- **Dash (-)**: Hold the pinch for a longer duration (0.5 to 1.5 seconds).
- **Letter Separation**: Pause for more than 1.5 seconds between gestures.

## How It Works

1. **Hand Detection**: The script captures video from the webcam and uses MediaPipe to detect hand landmarks.
2. **Gesture Recognition**: By tracking the distance between the index finger tip and thumb tip, it recognizes pinches and determines the duration to differentiate between dots and dashes.
3. **Morse Code Translation**: The captured Morse code is translated into corresponding characters and typed out using PyAutoGUI.

## Customization

You can modify the thresholds for gesture detection, the translation dictionary, or add new features like additional gesture commands by editing the main script.

## Contributions

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This project aims to explore the integration of computer vision and gesture recognition to create an innovative input method using Morse code. It can be particularly useful for accessibility applications or as a fun experiment in human-computer interaction.
