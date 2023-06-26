import cv2
import matplotlib.pyplot as plt
import numpy as np

def draw_circle(event, x, y, flags, param):

    # if a particular event occurs, do that
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,0,255), 5)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (255,0,0), 5)

cv2.namedWindow(winname = "my_drawing")
#callback
cv2.setMouseCallback("my_drawing", draw_circle) 





img = cv2.imread("../DATA/dog_backpack.jpg")

print("press q to quit")
while True:
    cv2.imshow("my_drawing", img)
    
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()