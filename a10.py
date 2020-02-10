#Point Processing:Log transform,Inverse Log Transform/Dynamic range Compression
import cv2
import matplotlib.pyplot as plt
import numpy as np
a,b=2,2#No of Subplots
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
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\img8.jpg',0)
show_img(img,'Original Image')
img_log=img.copy()
img_exp=img.copy()
r,c =img.shape[0],img.shape[1]
max_img=np.log(1+np.max(img))
for i in range(r):
    for j in range(c):
        img_log.itemset((i,j),(np.log(img.item(i,j)+1)/(max_img))*255)
        img_exp.itemset((i,j),10**((img.item(i,j)*max_img)/255-1))   
show_img(img_log,'Log Transform')
show_img(img_exp,' Inverse Log Transform')
plt.show()
