#Simple Read and Write Operations
import cv2
import matplotlib.pyplot as plt
#import numpy as np
a,b=3,3#No of Subplots
splot=1
def show_img(img,title=''):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    img_show = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_show, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis    
    plt.title(title)
plt.figure('First Practical')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\boy.bmp')
show_img(img,'Original Image')
show_img(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),'Gray Image')
img_b,img_g,img_r=img.copy(),img.copy(),img.copy()
img_b[:,:,1]=0;img_b[:,:,2]=0
img_g[:,:,0]=0;img_g[:,:,2]=0
img_r[:,:,0]=0;img_r[:,:,1]=0
show_img(img_r,'Red Component')
show_img(img_g,'Green Component')
show_img(img_b,'Blue Component')
plt.subplot(a,b,splot)
img_gray = cv2.cvtColor(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),cv2.COLOR_BGR2RGB)
plt.hist(img_gray.ravel(),256,[0,256])
splot+=1
plt.title('GrayScale Histogram')
plt.subplot(a,b,splot)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title("RBG Histogram")
splot+=1
plt.subplot(a,b,splot)
show_img(255-img_gray,'Negative of Image')
thresholding_parameter=127
r,c=img.shape[0],img.shape[1]
for i in range(r):
    for j in range(c):
        if img_gray.item(i,j,0)>=thresholding_parameter:
            img_gray.itemset((i,j,0),255)
        else:
            img_gray.itemset((i,j,0),0)
show_img(img_gray[:,:,0],'Binary Image')
plt.show()