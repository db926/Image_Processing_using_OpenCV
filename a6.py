#Manual  Histogram Equilization(Color)
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
def calcHist(img):
    l,w=img.shape[0],img.shape[1]
    N=l*w
    hist_l=np.zeros(256)
    pdf=np.zeros(256)
    for i in range(l):
        for j in range(w):
            it=img.item(i,j)
            hist_l[it]+=1
            pdf[it]=hist_l[it]/N
    n_hist=np.zeros(256)
    cdf=np.zeros(256)
    temp1=np.zeros(256)
    sumi=0
    for i in range(len(pdf)):
        sumi=sumi+hist_l[i]
        cdf[i]=sumi
        temp1[i]=cdf[i]/N
        n_hist[i]=round(temp1[i]*255)
    img_e=img.copy()
    for i in range(l):
        for j in range(w):
            img_e.itemset((i,j),n_hist[img.item(i,j)])
    return img_e,n_hist
plt.figure('Manual Histogram with Color')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\fruits.png')
show_img(img,'Original Image')
b_img=img[:,:,0]
g_img=img[:,:,1]
r_img=img[:,:,2]
img_b,hist_b=calcHist(b_img)
img_g,hist_g=calcHist(g_img)
img_r,hist_r=calcHist(r_img)

l,w=img.shape[0],img.shape[1]
N=l*w
img_s=img.copy()
for i in range(l):
    for j in range(w):
        img_s[i,j,0]=img_b[i,j]
for i in range(l):
    for j in range(w):
        img_s[i,j,1]=img_g[i,j]
for i in range(l):
    for j in range(w):
        img_s[i,j,2]=img_r[i,j]
show_img(img_s,'Histogram Equilized Image')

#Histograms of Color Bands
plt.figure('Histogram of Images')
a,b=2,3#No of Subplots
splot=1
color = ('b','g','r')
color_list=('Blue','Green','Red')
for i,col in enumerate(color):
    plotHistColor(img,i,col,color_list)
color = ('b','g','r')
color_list=('Blue','Green','Red')
for i,col in enumerate(color):
    plotHistColor(img_s,i,col,color_list)

plt.show()
