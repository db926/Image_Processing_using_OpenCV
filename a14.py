#Image Sharpening
import cv2
import matplotlib.pyplot as plt
import numpy as np
a,b=2,4#No of Subplots
splot=1
def show_img(img,title=''):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    # img_show = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis    
    plt.title(title)
plt.figure('Image Sharpening')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\soduku.png',0)
show_img(img,'Original Image')

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# sobelxy=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
show_img(laplacian,'laplacian Image')
show_img(sobelx,'sobelx Image')
show_img(sobely,'sobely Image')
# show_img(sobelxy,'sobelxy Image')
'''
There is a slight problem with that.
Black-to-White transition is taken as Positive slope (it has a positive value)
while White-to-Black transition is taken as a Negative slope
(It has negative value). So when you convert data to np.uint8,
all negative slopes are made zero. In simple words, you miss that edge.
'''

'''

# Output dtype = cv.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
# show_img(sobelx8u,'sobelx8u Image')
# show_img(sobel_8u,'sobel_8u Image')
'''
laplacian = img+laplacian
sobelx = img+sobelx
sobely = img+sobely
# sobelxy=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
show_img(laplacian,'Output laplacian Image')
show_img(sobelx,'Output sobelx Image')
show_img(sobely,'Output sobely Image')

plt.show()
