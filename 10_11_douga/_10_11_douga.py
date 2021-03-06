import numpy as np
import cv2

cap = cv2.VideoCapture('C:/human_detection/DCIM/MOV_0166_s.mpg')

#shrink the rectangle from default
def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        pad_w, pad_h = int(0.15 * w), int(0.05 * h)
        cv2.rectangle(img, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), thickness)


hog = cv2.HOGDescriptor() #derive HOG features
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #setSVMDetector

loop_count=0
bunsi=1
bunbo=2
ok=[0]*bunbo
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret :
      break
    #default detector
    

    #pedestrian detection
    #元コード
    #found, w = hog.detectMultiScale(frame, hitThreshold = 0, winStride = (8,8), padding = (0, 0), scale = 1.05, finalThreshold = 5)
    found, w = hog.detectMultiScale(frame, hitThreshold = 0.35, winStride = (8,8), padding = (0, 0), scale = 1.05, finalThreshold = 5)
    print(found)
    draw_detections(frame, found) #draw rectangles

    if (found !=()):
       ok[loop_count%bunbo]=1
    else:
       ok[loop_count%bunbo]=0
    loop_count+=1
    if sum(ok) >= bunsi and loop_count>=bunbo:
       print ('\007')

    #write & save frame
    cv2.imshow('original', frame) #write frame
    cv2.waitKey(1) #for keyboard binding
    #cv2.imwrite('test.jpg',frame) # save frame
    
cap.release()
cv2.destroyAllWindows()


#print cap.grab()


