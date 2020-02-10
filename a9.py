#Constast Stretching
import cv2
import matplotlib.pyplot as plt
import numpy as np
a,b=1,2#No of Subplots
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
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\cat.png',0)
show_img(img,'Original Image')

p1=(0,0)
p2=(150,20)
p3=(200,200)
p4=(255,255)
m1=(p1[1]-p2[1])/(p1[0]-p2[0])
m2=(p2[1]-p3[1])/(p2[0]-p3[0])
m3=(p3[1]-p4[1])/(p3[0]-p4[0])

c1=p1[1]-m1*p1[0]
c2=p2[1]-m2*p2[0]
c3=p3[1]-m3*p3[0]

#Transformation function
t=[]
for x in range(256):
    if(x<=p2[0]):
        t.append(m1*x+c1)
    if(x>p2[0] and x<=p3[0]):
        t.append(m2*x+c2)
    if(x>p3[0] and x<=p4[0]):
        t.append(m3*x+c3)
stret = img.copy()
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        stret[i,j]=t[img[i,j]];
show_img(stret,'Constrast Stretching')


plt.show()
