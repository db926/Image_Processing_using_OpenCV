#Bitwise Operations in Python
import cv2
import matplotlib.pyplot as plt
#import numpy as np
i=cv2.imread(r'D:\sem_6\IP\OpenCVPract\img7.jpg',0)
k=cv2.imread(r'D:\sem_6\IP\OpenCVPract\1bit1.png',0)
#plt.imshow(cv2.cvtColor(i,cv2.COLOR_BGR2RGB))
#print(i.shape)  
for ii in range(i.shape[0]):
    for  j in range(i.shape[1]):
        if(i[ii][j]>127):
            i[ii][j]=255
        else:
            i[ii][j]=0
plt.imshow(cv2.cvtColor(i,cv2.COLOR_BGR2RGB))
plt.title("1st Image")
plt.figure() 
plt.imshow(cv2.cvtColor(k,cv2.COLOR_BGR2RGB))
plt.title("2nd Image")
plt.figure()
i=cv2.resize(i,(k.shape[1],k.shape[0]))
#print(i.shape,k.shape)
o=cv2.bitwise_and(k,i,mask=None)
plt.title("Bitwise AND Result")
plt.imshow(cv2.cvtColor(o,cv2.COLOR_BGR2RGB))
plt.figure()
oor=cv2.bitwise_or(k,i,mask=None)
plt.title("Bitwise OR Result")
plt.imshow(cv2.cvtColor(oor,cv2.COLOR_BGR2RGB))
plt.figure()
oor=cv2.bitwise_xor(k,i,mask=None)
plt.title("Bitwise XOR Result")
plt.imshow(cv2.cvtColor(oor,cv2.COLOR_BGR2RGB))
plt.figure()

oor=cv2.bitwise_not(i,mask=None)
plt.title("Bitwise NOT Result")
plt.imshow(cv2.cvtColor(oor,cv2.COLOR_BGR2RGB))
plt.show()