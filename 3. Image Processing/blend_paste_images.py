import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread("../DATA/dog_backpack.png")
img2 = cv2.imread("../DATA/watermark_no_copy.png")

# convert them to RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) # (1401, 934, 3)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) # (1280, 1277, 3)

plt.imshow(img1)
plt.title("img 1")
plt.show()

plt.imshow(img2)
plt.title("img 2")
plt.show()

print("be aware that they are not in the same size")

# resize
resized_img1 = cv2.resize(img1, (1200, 1200))
resized_img2 = cv2.resize(img2, (1200, 1200))

# show them again
plt.imshow(resized_img1)
plt.title("resized img 1")
plt.show()

plt.imshow(resized_img2)
plt.title("resized img 2")
plt.show()

# lets blend them using addWeighted: src1, alpha, src2, beta, gamma
blended = cv2.addWeighted(src1 = resized_img1, alpha = 0.8, src2 = resized_img2, beta = 0.2, gamma = 0)
plt.imshow(blended)
plt.title("blended image")
plt.show()

# overlay small image on top of a larger image (no blending)
# numpy reassignment

# define the sizes, a large and a small image
large_img = img1.copy()
small_img = cv2.resize(img2, (600,600)) # (600,600,3)

# starting points, I want to start from the top right
x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end, x_offset:x_end] = small_img

print("the watermark is resized to be small and inserted to the top right part")
plt.imshow(large_img)
plt.title("Overlay image, no blending")
plt.show()

# what is I want to mask the part of an image and insert?

# blend together images of different sizesü

# define the sizes, a large and a small image
large_img = img1.copy() # (1401, 934, 3)
small_img = cv2.resize(img2, (600,600)) # (600,600,3)

# I want to insert it to the bottom right
x_offset = 934 - 600 
y_offset = 1401 - 600

rows, cols, channels = small_img.shape

roi = large_img[y_offset:1401, x_offset:943]

plt.imshow(roi)
plt.title("roi, bottom right of the large img")
plt.show()

# get the grayscale version of the small img
small_img_gray = cv2.cvtColor(small_img, cv2.COLOR_RGB2GRAY)

# plot it, you need to say its gray (use cmap)
plt.imshow(small_img_gray, cmap="gray")
plt.title("grayscale watermark image")
plt.show()

# built the mask, everything is either black or white
mask_inv = cv2.bitwise_not(small_img_gray)

plt.imshow(mask_inv, cmap = "gray")
plt.show()

print(f"mask_inv has no longer 3 channels: {mask_inv.shape}")

# fill with 255 with the shape of small_img_gray
white_background = np.full(small_img_gray.shape, 255, dtype = np.uint8) # (600, 600, 3)

background = cv2.bitwise_or(src1 = white_background, src2 = white_background, mask = mask_inv) # (600, 600, 3)

plt.imshow(background, cmap = "gray")
plt.title("actual background")
plt.show()

foreground = cv2.bitwise_or(small_img, small_img, mask = mask_inv)

plt.imshow(foreground)
plt.title("foreground")
plt.show()

final_roi = cv2.bitwise_or(roi, foreground)

plt.imshow(final_roi)
plt.title("watermark on roi using bitwise_or")

# now set this roi onto the larger image

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = final_roi
plt.imshow(large_img)
plt.title("final image")
plt.show()
