import cv2
from ultralytics import YOLO
import random
import time
import os
import numpy as np
from PIL import Image
from mss import mss

#pip install mss

def process_real_time_detection(model, show=True):
    # Open the input screen handler
    sct = mss()
    start_time = time.time()
    #x и counter для счетчика фпс раз в 5 секунд вывод
    x = 5 
    counter = 0

    while True:
        w, h = 1000, 800
    #set the capture position
        monitor = {'top': 0, 'left': 0, 'width': w, 'height': h}
        img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        #просто счетчик фпс
        counter+=1
        if (time.time() - start_time) > x :
            print("FPS: ", counter / (time.time() - start_time))
            counter = 0
            start_time = time.time()
        
        results=model.track(frame, iou=0.4, conf=0.5, persist=True, imgsz=608, verbose=False, tracker="botsort.yaml")      
        if results[0].boxes.id != None: # this will ensure that id is not None -> exist tracks
            boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
            ids = results[0].boxes.id.cpu().numpy().astype(int)
            
            for box, id in zip(boxes, ids):
                # Generate a random color for each object based on its ID
                random.seed(int(id))
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3],), color, 2)
                cv2.putText(
                    frame,
                    f"Id {id}",
                    (box[0], box[1]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 255),
                    2,
                )                
        if show:
            frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)
            cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Example usage:
model = YOLO('yolo/best.pt')
model.fuse()
process_real_time_detection(model,show=True)