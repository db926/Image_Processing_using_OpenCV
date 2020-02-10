#Power law Transformation
import cv2
import matplotlib.pyplot as plt
import numpy as np
a,b=2,1#No of Subplots
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
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\boy.bmp',0)
show_img(img,'Original Image')
img_out=img.copy()
r,c =img.shape[0],img.shape[1]
gamma=1.1
c=1
img_out=c*img**gamma
img_out=img_out.astype('uint8')
show_img(img_out,'Power law Transformation')
plt.show()
