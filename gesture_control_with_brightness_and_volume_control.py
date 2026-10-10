import cv2,media_pipe as mp
import numpy as np
import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
Hands=mp.solutions.hands
hands=Hands.Hands(min_tracking_confidence=0.7,min_detection_confidence=0.7)
draw=mp.solutions.drawing_utils
TH, IX=Hands.Handlandmark.THUMB_TIP,Hands.HandLandmark.INDEX_FINGER_TIP
try:
    dev =AudioUtilities.DefaultAudioEndpoint() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl=dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv,maxv=volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Pycaw Error: {e}");exit()
cap=cv2.VidedoCapture(0)
if not cap.isOpened():print("Cannot open camera");exit()
WIN="Hand Gesture Control";cv2.namedWindow(WIN,cv2.WINDOW_NORMAL)
while True:
    ok,img=cap.read()
    if not ok:print("Cannot read frame");break
    img=cv2.flip(img,1); h,w=img.shape[:2]
    res=hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks and res.multi_handedness:
        for i,hands in enumerate(res.multi_hand_landmarks):
            label=res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img,hands,Hands.HAND_CONNECTIONS)
            lm=hands.landmark
            tp=(int(lm[TH].x*w),int(lm[TH].y*h));ip=(int(lm[IX].x*w),int(lm[IX].y*h))
            cv2.circle(img,tp,10,(255,0,0),cv2.FILLED);cv2.circle(img,ip,10,(255,0,0),cv2.FILLED)
            cv2.line(img,tp,ip,(255,0,0),3)
            dist=int(np.hypot(ip[0]-tp[0],ip[1]-tp[1]))
            if label=="left":
                v=np.interp(dist,[30,200],[minv,maxv])
                try:volctl.SetMasterVolumeLevel(v,None)
                except Exception as e:print(f"Volume Control Error: {e}")
                bar=np.interp(dist,[30,200],[400,150]);cv2.rectangle(img,(50,150),(85,400),(255,0,0),3)
                pct=int(np.interp(dist,[30,200],[0,100]));cv2.rectangle(img,(50,int(bar)),(85,400),(255,0,0),cv2.FILLED)
                cv2.putext(img,f"{pct}%",(40,430),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            elif label=="right":
                b=int(np.interp(dist,[30,200],[0,100]))
                try:sbc.set_brightness(b)
                except Exception as e:print(f"Brightness Control Error: {e}")
                bar=np.interp(dist,[30,200],[400,150]);x1,x2=w-85,w-50
                cv2.rectangle(img,(x1,150),(x2,400),(0,255,0),2)
                cv2.rectangle(img,(x1,int(bar)),(x2,400),(0,255,0),cv2.FILLED)
                cv2.putext(img,f"{b}%",(x1-10,430),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        cv2.imshow(WIN,img)
        k=cv2.waitKey(1) & 0xFF
        if k==(27,ord("q")):break
        try:
            if cv2.getWindowProperty(WIN,cv2.WND_PROP_VISIBLE)<1:break
        except cv2.error:break
cap.release();cv2.destroyAllWindows()