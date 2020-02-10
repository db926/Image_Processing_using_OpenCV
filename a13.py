#Averaging Filter and Median Filter
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
a,b=2,4#No of Subplots
splot=1
def show_img(img,title=''):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    img_show = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_show, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis    
    plt.title(title)
plt.figure('Point Processing Gray Scale')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\lena.png',0)
show_img(img,'Original Image')

# Adding Salt and Pipper Noise
def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
img=sp_noise(img,0.05)
show_img(img,'Noisy Image')



kernel = np.ones((5,5),np.float32)/25
img_filt2d = cv2.filter2D(img,-1,kernel)
show_img(img_filt2d,'Averaging Filter using filter2D')
'''
The Above method is Generalized Method For Image Filtering using Kernal 
can be applied to any Image 

-1 indicates desired depth of the destination image as src.depth()
'''

img_blur = cv2.blur(img,(5,5))#5*5 Box Filter Equivalent of Above
# img_boxFilter = cv2.boxFilter(img,-1,(5,5))#Used when we want to normalize='false'
show_img(img_blur,'Averaging Filter using blur')
# show_img(img_boxFilter,'Averaging Filter using boxFilter')

img_gblur=cv2.GaussianBlur(img,(5,5),0)# Border=0,we can also specify sigmaX &Y
show_img(img_blur,'Averaging Filter using GaussianBlur')
'''
a=cv2.getGaussianKernel(5,1)
b=cv2.sepFilter2D(img,-1,a,a)
cv2.imshow('',b)
cv2.waitKey(0)
# show_img(b,'Averaging Filter using GaussianBlur')
'''
img_med=cv2.medianBlur(img,5)
show_img(img_med,' Filter using median filter')
# For Edges
img_bilateral=cv2.bilateralFilter(img,9,75,75)
show_img(img_bilateral,' Filter using bilateralFilter')


plt.show()