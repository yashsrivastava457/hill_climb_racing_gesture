import cv2
import mediapipe as mp
import pyautogui


def control(gesture):
    if gesture == "ACCELERATE":
        pyautogui.keyUp("left")
        pyautogui.keyDown("right")
        
    elif gesture == "BRAKE":
        pyautogui.keyUp("right")
        pyautogui.keyDown("left")
    else:
        pyautogui.keyUp("right")
        pyautogui.keyUp("left")

cam = cv2.VideoCapture(0)
cv2.namedWindow("Gesture" , cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gesture" , 800 , 600)

mp_hands= mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=False,
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

while True:
    success , frame = cam.read()
    
    if not success:
        print("Camera not detected")
        break
        
    # frame = cv2.flip(frame , 1)
        
    img_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    
    results = hands.process(img_rgb)
    
    
    if results.multi_hand_landmarks:
        for hand_index , hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_draw.draw_landmarks(frame , hand_landmarks , mp_hands.HAND_CONNECTIONS )
            #landmark object
            
            landmarks = hand_landmarks.landmark
            
            #index finger
            index_open = landmarks[6].y>landmarks[8].y
            #middle finger
            middle_open = landmarks[10].y>landmarks[12].y
            #ring finger
            ring_open = landmarks[14].y>landmarks[16].y
            #small finger
            small_open = landmarks[18].y>landmarks[20].y
            
            #thumb
            hand_label = results.multi_handedness[hand_index].classification[0].label
            
            if hand_label=="Right":
                thumb_open = landmarks[3].x>landmarks[4].x
            else:
                thumb_open = landmarks[3].x<landmarks[4].x
                
            
            
            
            palm = sum([index_open,middle_open,ring_open,small_open,thumb_open])
            
            if palm == 0:
                gesture = "BRAKE"
            
            elif palm == 5:
                gesture ="ACCELERATE"
            else:
                gesture = "NONE"
                
            control(gesture)
                
                
            
    
    cv2.imshow("Gesture" , frame)
    if (cv2.waitKey(1) and 0xff) == ord('q'):
        break
    
    
hands.close()
cam.release()
cv2.destroyAllWindows()
