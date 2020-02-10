#Manual  Histogram Equilization(Color and Gray Scale)
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


plt.figure('Manual Histogram GrayScale')
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\lena.png')
show_img(img,'Original Image')
t_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
show_img(t_img,'Gray Scale Image')
plotHist(t_img)
img_e,hist_n=calcHist(t_img)
show_img(img_e,'Histogram Equilized Image')
plotHist(img_e)

# For Automated Histogram Calculation
# plt.hist(img.ravel(),256,[0,256]); 
# For Histogram Equilization
img_eq=cv2.equalizeHist(t_img)
show_img(img_eq,'Histogram Equilized Image using equalizeHist')

plt.show()
