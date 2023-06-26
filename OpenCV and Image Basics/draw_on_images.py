import cv2
import matplotlib.pyplot as plt
import numpy as np

#part1
blank_img = np.zeros((512,512,3))

print("-see the blank image")
plt.imshow(blank_img)
plt.show() 

# no need to set the variable
# if you specify thickenss as -1, it fills the shape
cv2.rectangle(blank_img, pt1 = (300, 320), pt2 = (480,400), color = (0,255,0), thickness = 10)
#color is up to you

print("-see the rectangle")
plt.imshow(blank_img)
plt.show()

# ususally used in object detection
cv2.rectangle(blank_img, pt1 = (200,200), pt2 = (300,300), color = (0,0,255), thickness = 5)
print("-see the square (usually used in object detection)")
plt.imshow(blank_img)
plt.show()

cv2.circle(blank_img, center = (100,100), radius = 50, color = (255,0,0), thickness = 7)
print("-see the circle")
plt.imshow(blank_img)
plt.show()

cv2.line(blank_img, pt1 = (512,512), pt2 = (0,0), color = (132, 200, 165), thickness = 3)
print("-see the line")
plt.imshow(blank_img)
plt.show()

#part2
# write text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text = "Hello", org = (90, 500), fontFace = font, 
            fontScale = 4, color = (255,255,255), 
            thickness = 3, lineType = cv2.LINE_AA)

plt.imshow(blank_img)
plt.show()

# draw ploygon
print("new blank image")
blank_img = np.zeros(shape = (512,512,3))

# (4,2)
vertices = np.array( ([100,300], [200,200], [400,300], [200,400]), dtype=np.int32 )

# opencv wants the shape of the vertices to be 3 dimention
pts = vertices.reshape(-1,1,2) # -1: whatever it takes
# (4, 1, 2)

# you have to pass pts as list
cv2.polylines(blank_img, [pts], isClosed = True, color = (255,0,0), thickness = 5)
plt.imshow(blank_img)
plt.show()