import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):

    # if a particular event occurs, do that
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,0,255), -1)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (255,0,0), -1)

drawing = False # will be true when you click the mouse
ix, iy =  -1, -1
def draw_rectangle(event, x,y, flags, params):
    # keep track these global variables: 
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN: # if thats true, we are drawing
        drawing == True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # it will draw the current rectangle, will be smooth.
            cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # redrawing the final rectangle
        cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)

cv2.namedWindow(winname = "my_drawing")
#callback
cv2.setMouseCallback("my_drawing", draw_rectangle) # change the function if you desire

img = np.zeros((512,512,3), np.int8) # int8 makes background less dark

print("press q to quit")
while True:
    cv2.imshow("my_drawing", img)
    
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()

