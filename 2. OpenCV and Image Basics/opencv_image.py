import numpy as np
import matplotlib.pyplot as plt
import cv2

# be careful, this will not cause and error but return a NoneType
# img = cv2.imread("path/doesnot/exist")
# print(type(img))

# the image is read by cv2
img = cv2.imread("../DATA/00-puppy.jpg")
print(type(img))
print("the type of the return cv2 imread is a numpy array.")

# visualize with matplotlib
print("The image is printed weird because cv2 reads images in BGR order while matplotlib displays it as if RGB")
plt.imshow(img)
plt.show()

# to show it as normal, we need to convert the channels, start with "COLOR_"
fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("Now it seems nice")
plt.imshow(fixed_img)
plt.show()

# visualize with cv2
# you have to provide the definition, otherwise you will get an error.
print("This is how opencv reads the initial image")
#opencv displaysm the real image sizes, you cant resize it.
cv2.imshow("show", img)
cv2.waitKey(0)

# you can read images with different format, start with "IMREAD_"
img_gray = cv2.imread("../DATA/00-puppy.jpg", cv2.IMREAD_GRAYSCALE)

print("how matplotlib sees the grayscale images without cmap=gray")
plt.imshow(img_gray)
plt.show()

print("now it is grayscale with cmap=gray")
plt.imshow(img_gray, cmap = "gray")
plt.show()

print("see it with cv2 imread")
cv2.imshow("grayscale", img_gray)
cv2.waitKey(0)

# how to resize the image
print("this is a resized image usigng cv2")
resized_img = cv2.resize(fixed_img, (1000,400))
print(resized_img.shape)
plt.imshow(resized_img)
plt.show()

print("resized image by 50 percent ratio")
h_ratio = 0.5
w_ratio = 0.5
resized_img = cv2.resize(fixed_img, (0,0), fixed_img, w_ratio, h_ratio)
print(resized_img.shape)
plt.imshow(resized_img)
plt.show()

# flip images, used to generate images for deep learning
print("horizontal: 0 , vertical: 1, both: -1")
for num in [0, 1, -1]:
    flip_img = cv2.flip(fixed_img, num)
    cv2.imshow(f"flip type {num}", flip_img)
    print(f"flip type {num}")
    cv2.waitKey(0)


# write image in a file, (path, img)
cv2.imwrite("new_file.jpg", fixed_img)

# this section may be related to the jupyter notebook, did not work on .py
# fig = plt.figure(figsize = (5,4))
# ax = fig.add_subplot(111)
# print("this is how to let the matplotlib show img larger")
# ax.imshow(fixed_img)
# ax.plot()