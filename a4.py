#Manual Plotting Histogram (Color and Gray Scale)
import cv2
import matplotlib.pyplot as plt
import numpy as np
a,b=2,3#No of Subplots
splot=1
def show_img(img,title=''):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    img_show = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_show, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis    
    plt.title(title)
def plotHist(img):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    l,w=img.shape[0],img.shape[1]
    hist_l=np.zeros(256)
    for i in range(l):
        for j in range(w):
            hist_l[img.item(i,j)]+=1
    plt.bar(np.arange(0,256,1),hist_l,color='black')
    plt.title('Gray Scale Histogram')
def plotHistColor(img,c,col,cl):
    global splot
    plt.subplot(a,b,splot)
    splot+=1
    l,w=img.shape[0],img.shape[1]
    hist_l=np.zeros(256)
    for i in range(l):
        for j in range(w):
            hist_l[img.item(i,j,c)]+=1
    plt.bar(np.arange(0,256,1),hist_l,color=col)
    st_t=cl[c]+' Scale Histogram'
    plt.title(st_t)
plt.figure('Manual Histogram')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\cat.png')
show_img(img,'Original Image')
t_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
show_img(t_img,'Gray Scale Image')
plotHist(t_img)
color = ('b','g','r')
color_list=('Blue','Green','Red')
for i,col in enumerate(color):
	plotHistColor(img,i,col,color_list)
plt.show()
