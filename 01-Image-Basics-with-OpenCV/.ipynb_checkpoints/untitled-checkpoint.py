import cv2
import numpy as np

def create_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),thickness=10)
        
img = cv2.imread("DATA/dog_backpack.png")

cv2.namedWindow(winname='dog')

cv2.setMouseCallback('dog',create_circle)

while True:
    cv2.imshow('dog',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()