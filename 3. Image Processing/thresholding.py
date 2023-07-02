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


img = cv2.imread("../DATA/crossword.jpg", 0) 
plt.imshow(img, cmap="gray")
plt.title("grayscale crossword image")
plt.show()

print("To distinguish the grey background in the crossword image, apply binary thresholding")

ret, thresh_img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
plt.imshow(thresh_img, cmap = "gray")
plt.title("thresholded crossword image")
plt.show()

thresh2_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8) #image, max_value, adaptive method, threshold type, block size, decreased_value
plt.imshow(thresh2_img, cmap = "gray")
plt.title("Adaptive thresholding with mean")
plt.show()

print("blend the thresholdings")

blended = cv2.addWeighted(src1 = thresh_img, alpha = 0.4, src2 = thresh2_img, beta = 0.6, gamma = 0)
plt.imshow(blended, cmap = "gray")
plt.title("blended image from binary thresholding and adaptive thresholding, usually results better.")
plt.show()