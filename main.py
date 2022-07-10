import pyvirtualcam
import numpy as np
from PIL import Image
import cv2

specs = {'left':0,'top':0,'width':1920,'height': 1080}
ang = 0
with pyvirtualcam.Camera(width=1280, height=720, fps=60) as cam:
    print("Setting up Camera:")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ang+=1
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        ang%36
        frame = frame.rotate(ang)
        cam.send(np.asarray(frame))
        cam.sleep_until_next_frame()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
