#Bit Plane Slicing
import cv2
import matplotlib.pyplot as plt
import  math
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
plt.figure('Bit Plane Slicing Practical')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\cameraman.tif',0)
show_img(img,'Original Image')
iarr=[]
for i in range(8):
    iarr.append(img.copy())
r,c=img.shape[0],img.shape[1]
for k in range(8):
	for i in range(r):
	    for j in range(c):
	        t=img.item(i,j)
	        x=bin(t)
	        x=x.replace('0b','')
	        if len(x)<8:
	            x='0'*(8-len(x))+x
	        if x[k]=='0':
	            iarr[k].itemset((i,j),0)
	        elif x[k]=='1':
	            iarr[k].itemset((i,j),255)
	show_img(iarr[k],k)
plt.show()