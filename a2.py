#Gray Level Slicing/ Intensity Level Slicing
import cv2
import matplotlib.pyplot as plt
#import numpy as np
a,b=1,3#No of Subplots
splot=1
def show_img(img,title=''):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    img_show = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_show, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis    
    plt.title(title)
plt.figure('Gray Level Slicing Practical')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\boy.bmp',0)
show_img(img,'Original Image')
thes_a=100
thes_b=150
r,c=img.shape[0],img.shape[1]
for i in range(r):
    for j in range(c):
        if img.item(i,j)>thes_a and img.item(i,j)<thes_b:
            img.itemset((i,j),255)
        else:
            img.itemset((i,j),0)
show_img(img,'Bit Plane Slicing without Background')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\boy.bmp',0)            
r,c=img.shape[0],img.shape[1]
for i in range(r):
    for j in range(c):
        if img.item(i,j)>thes_a and img.item(i,j)<thes_b:
            img.itemset((i,j),255)
show_img(img,'Bit Plane Slicing with Background')
plt.show()