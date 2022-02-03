import cv2 as cv
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)

mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mpHands = mp.solutions.hands
hands=mpHands.Hands()

capture = cv.VideoCapture(0)
 

while True:
    isTrue, frame=capture.read()
    img_rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=hands.process(img_rgb)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList=[]
            for id , lm in enumerate(handLms.landmark):
                # print(id ,lm)
                h ,w ,c=frame.shape
                cx,cy=int(lm.x *w),int(lm.y*h) 
                # print(id,cx,cy)
                lmList.append([id,cx,cy])
            # print(lmList)
            # mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            if lmList:
                x1,y1=lmList[4][1],lmList[4][2]
                x2,y2=lmList[8][1],lmList[8][2]
            cv.circle(frame,(x1,y1),5,(0,0,255),-1)
            cv.circle(frame,(x2,y2),5,(0,0,255),-1)
            cv.line(frame,(x1,y1),(x2,y2),(0,0,255),3)
            length=math.hypot(x2-x1,y2-y1)
            print(length)
            volrange = volume.GetVolumeRange()
            minVol = volrange[0]
            maxVol=volrange[1]
            vol=np.interp(length,[50,300],(minVol,maxVol))
            volume.SetMasterVolumeLevel(vol,None)
    cv.imshow("Image",frame)
    if cv.waitKey(1) & 0xff==ord('d'):        
        break
capture.release()
cv.destroyAllWindows()


