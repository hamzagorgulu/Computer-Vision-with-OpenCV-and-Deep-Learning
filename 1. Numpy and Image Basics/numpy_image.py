# types of image: grayscale images and color images

# numpy cant directly read images such as jpg, png, etc. So we need to use a library called PIL (Python Imaging Library)

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open("../DATA/00-puppy.jpg")
print(type(pic)) #a jpeg image, not a numpy array

pic_arr = np.asarray(pic)

print(type(pic_arr))

# to visualize a numpy array
print("the actual image")
plt.imshow(pic_arr)
plt.show()

pic_red = pic_arr.copy()

print("see the channels")

# seeing like this doesnt actually makes sense bc matplotlib doesnot know which channel the input represents. To see them as red, blue, or green, you should set the rest to 0
for ch_size in range(3):
    # cmpap = "gray" means show that image in the grayscale mode.
    plt.imshow(pic_red[:,:,ch_size]) # the order of the channels: R G B
    plt.title(f"channel size {ch_size}, this is 1D img")
    plt.show()


# lets say I want to visualize the red channel
# set all values in the green channel 0
pic_red[:, :, 1] = 0
# then set all values in the blue to 0
pic_red[:, :, 2] = 0
#see the how the final image(red) looks like, it is still 3 channel size bc we only set some to 0.
print("red image, by deleting the green and blue channels, remember that this img has still 3 channel size")
plt.imshow(pic_red)
plt.title('red image, this is 3D')
plt.show()