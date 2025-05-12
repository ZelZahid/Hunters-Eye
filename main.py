import cv2 as cv
import pyautogui
import mss
import numpy as np
import time

w, h = pyautogui.size()
print("screen Resulution:", w,'x', h)
img = None
t0 = time.time()
n_frames = 1
#test
monitor = {"top":0, "left":0, "width": w, "height": h}

with mss.mss() as sct:
    while True:
        img = sct.grab(monitor)
        img = np.array(img)
        small = cv.resize(img, (0,0), fx = 0.5, fy = 0.5)
        cv.imshow("Computer Vision", small)

        #end test
        key = cv.waitKey(1)
        if key == ord('q'):
            break
    
        elapsed_time = time.time() - t0
        avg_fps = (n_frames / elapsed_time)
        print("Average FPS: " + str(avg_fps))
        n_frames += 1