import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread("../DATA/rainbow.jpg", 0) # 0 means read as grayscale
plt.imshow(img_gray, cmap = "gray")
plt.title("initial grayscale image")
plt.show()


# lets threshold the grayscale img: img, threshold value, possible max_value, thesholding type
ret, thresh1 = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY) # THRESH_BINARY_INV, THRESH_TRUNC
# ret is the thresholding value

plt.imshow(thresh1, cmap="gray")
plt.title("thresholded grayscale img")
plt.show()