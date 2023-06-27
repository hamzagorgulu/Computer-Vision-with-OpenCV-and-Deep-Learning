import cv2
import matplotlib.pyplot as plt

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
large_img = img1
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

