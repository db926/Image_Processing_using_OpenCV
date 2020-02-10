#Manual Min Max Filter
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.exposure import rescale_intensity
a,b=3,1#No of Subplots
splot=1
def show_img(img,title=''):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    img_show = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis    
    plt.title(title)

def max_convolve(image):
	(iH, iW) = image.shape[:2]
	kernel = np.array((
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]), dtype="int")
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi).max()
			output[y - pad, x - pad] = k
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output
def min_convolve(image):
	(iH, iW) = image.shape[:2]
	kernel = np.array((
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]), dtype="int")
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi).min()
			output[y - pad, x - pad] = k
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output
plt.figure('Image Sharpening')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\soduku.png',0)
show_img(img,'Original Image')
maxi=max_convolve(img)
mini=min_convolve(img)
show_img(maxi,'Max Filter')
show_img(mini,'Min Filter')

plt.show()
