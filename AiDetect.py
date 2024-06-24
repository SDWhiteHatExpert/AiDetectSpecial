import cv2
import mediapipe as mp
import pyautogui
import time

# Morse Code Dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}

def translate_morse(morse_code):
    return MORSE_CODE_DICT.get(morse_code, '')

def main():
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()

    # Morse code variables
    morse_code = ''
    last_gesture_time = time.time()
    gesture_start_time = 0
    detecting_morse = False

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                landmarks = hand.landmark
                index_x, index_y, thumb_x, thumb_y = 0, 0, 0, 0

                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)

                    if id == 8:  # Index finger tip
                        cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y

                    if id == 4:  # Thumb tip
                        cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y

                distance = abs(index_y - thumb_y)

                if distance < 20:  # Close gesture (potential Morse code)
                    if not detecting_morse:
                        gesture_start_time = time.time()
                        detecting_morse = True
                else:
                    if detecting_morse:
                        gesture_duration = time.time() - gesture_start_time
                        if gesture_duration < 0.5:
                            morse_code += '.'
                        elif 0.5 <= gesture_duration < 1.5:
                            morse_code += '-'
                        else:
                            if morse_code:
                                print(f"Morse Code: {morse_code}")
                                translated_char = translate_morse(morse_code)
                                print(f"Translated: {translated_char}")
                                pyautogui.write(translated_char)
                                morse_code = ''
                        detecting_morse = False
                        last_gesture_time = time.time()

        # Check for end of Morse code input (space between letters/words)
        if time.time() - last_gesture_time > 1.5 and morse_code:
            print(f"Morse Code: {morse_code}")
            translated_char = translate_morse(morse_code)
            print(f"Translated: {translated_char}")
            pyautogui.write(translated_char)
            morse_code = ''

        cv2.imshow("Virtual Mouse with Morse Code", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
