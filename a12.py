#Geometric Operations
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
img =cv2.imread(r'D:\sem_6\IP\OpenCVPract\boy.bmp',0)
show_img(img,'Original Image')
img_out=img.copy()
r,c =img.shape[0],img.shape[1]
center = (r / 2, c / 2)

# For Rotation
angle=45
M = cv2.getRotationMatrix2D(center,angle,1.0)
img_rotate=cv2.warpAffine(img, M, (c, r))
show_img(img_rotate,'For Rotation')

# For Scaling
Scale =1.5
M = cv2.getRotationMatrix2D(center,0,Scale)
img_scale=cv2.warpAffine(img, M, (c, r))
show_img(img_scale,'For Scaling')

# For Translation
tx=100
ty=50
M=np.float32([[1,0,tx],[0,1,ty]])
img_tras=cv2.warpAffine(img, M, (c, r))
show_img(img_tras,'For Translation')
plt.show()

'''
General Form of M which is the transformation Matrix is
[ s*cos(x)  s*sin(x) tx]
[-s*sin(x)  s*cos(x) ty]
Here tx and ty =tx and ty(Assumed above) 
only if center is at mid and x=0 making sin and cos 0 and 1 
'''
