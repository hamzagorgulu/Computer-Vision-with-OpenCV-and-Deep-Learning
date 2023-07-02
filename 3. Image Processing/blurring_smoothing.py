import cv2
import numpy as np
import matplotlib.pyplot as plt

# what we are gonna do is to blur the image

def load_img():
    img = cv2.imread("../DATA/bricks.jpg").astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_img(img, title = ""):
    plt.imshow(img)
    plt.title(title)
    plt.show()

img = load_img()
display_img(img, "the initial brick image")

gamma = 1/4 #increasing or decreasing the brightness of the image
result = np.power(img, gamma) # every pixel will be the power of gamma of each pixel.
display_img(result, f"blurred image with gamma = {gamma}")

# load it again
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
# write bricks on top of the image (img, the text, location, font, font scale, color, thickness)
img_font = cv2.putText(img, text = "bricks", org = (10,600), fontFace = font, fontScale = 5, color = (255,0,0), thickness = 4)
display_img(img_font, "Image with a text on top of it.")

# see how it differs with kernels
kernel = np.ones(shape=(5,5), dtype = np.float32) / 25 # every value is 0.04
destination = cv2.filter2D(img, -1, kernel) # -1 means I want the output depth to be the same as input depth
display_img(destination, "blurring with custom kernel")


# load it again
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
# write bricks on top of the image (img, the text, location, font, font scale, color, thickness)
img_font = cv2.putText(img, text = "bricks", org = (10,600), fontFace = font, fontScale = 5, color = (255,0,0), thickness = 4)
blurred = cv2.blur(img_font, ksize = (5,5))
display_img(blurred, "blurring with cv2.blur method, with 5x5 kernel")

# gaussian blurring
# load it again
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
# write bricks on top of the image (img, the text, location, font, font scale, color, thickness)
img_font = cv2.putText(img, text = "bricks", org = (10,600), fontFace = font, fontScale = 5, color = (255,0,0), thickness = 4)
blurred_img = cv2.GaussianBlur(img, (5,5), 10) # img, kernel size, sigma value
display_img(blurred_img, "Blurring with Gaussian blur")


median_result = cv2.medianBlur(img, 5)
display_img(median_result, "Blurred image with median blur.")


img = cv2.imread("../DATA/sammy.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
display_img(img, "display the initial dog image")

noise_img = cv2.imread("../DATA/sammy_noise.jpg")
display_img(img, "display the noise added dog image")

print("lets use the median blur to fix the noise")

median = cv2.medianBlur(noise_img, 5)
display_img(median, "median blur over the noised image, it actuall reduces the noise")

# performing bilateral filter
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
# write bricks on top of the image (img, the text, location, font, font scale, color, thickness)
img_font = cv2.putText(img, text = "bricks", org = (10,600), fontFace = font, fontScale = 5, color = (255,0,0), thickness = 4)
blur = cv2.bilateralFilter(img_font, 9, 75, 75)
display_img(blur, "blurred img using bilateral filter")