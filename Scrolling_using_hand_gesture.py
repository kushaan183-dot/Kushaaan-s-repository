import cv2, time, pyautogui
import mediapipe as mp
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing=mp.solutions.drawing_utils
SCROLL_SPEED=300
SCROLL_DELAY=1
CAMERA_WIDTH,CAM_HEIGHT=640,480
def detect_gesture(landmarks,handedness):
    fingers=[]
    tips=[mp.hands.HandLandmark.INDEX_FINGER_TIP,mp.hands.HandLandmark.MIDDLE_FINGER_TIP,mp.hands.HandLandmark.RING_FINGER_TIP,mp.hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if landmarks.landmarks[tip].y<landmarks.landmarks[tip-2].y:
            fingers.append(1)
        thumb_tip=landmarks.landmarks[mp.hands.HandLandmark.THUMB_TIP]
        thumb_ip=landmarks.landmarks[mp.hands.HandLandmark.THUMB_IP]
        if (handedness=="right"and thumb_tip.x>thumb_ip.x) or (handedness=="left" and thumb_tip.x<thumb_ip.x):
            fingers.append(1)
        return "scroll up" if sum(fingers)==5 else "scroll down" if len(fingers)==0 else "none"
cap=cv2.VideoCapture(0)
cap.set(3,CAMERA_WIDTH)
cap.set(4,CAM_HEIGHT)
last_scroll_time=p_time=0
print("Gesture Scroll Control Active\nOpen palm: Scroll Up\nFist: ScrollDown\nPress 'q' to exit")
while cap.isOpened():
    success,img=cap.read()
    if not success:break
    img=cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
    results=hands.process(img)
    gesture,handedness="none","unknown"
    if results.multi_hand_landmarks:
        for hand_landmarks,hand_handedness in zip(results.multi_hand_landmarks,results.multi_handedness):
            handedness=hand_handedness.classification[0].label
            gesture=detect_gesture(hand_landmarks,handedness)
            mp_drawing.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)

            if (time.time()-last_scroll_time)>SCROLL_DELAY:
                if gesture=="scroll up":pyautogui.scroll(SCROLL_SPEED)
                elif gesture=="scroll down":pyautogui.scroll(-SCROLL_SPEED)
                last_scroll_time=time.time()
    fps=1/(time.time()-p_time) if p_time>0 else 0
    p_time=time.time()
    cv2.putText(img,f"FPS: {int(fps)} | Hand: {handedness} | Gesture: {gesture}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.imshow("Gesture Scroll Control",cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1)&0xFF==ord('q'):break
cap.release()
cv2.destroyAllWindows()
