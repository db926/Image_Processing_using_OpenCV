#Arithmetic Operations in Python
import cv2
import matplotlib.pyplot as plt
import numpy as np
i=cv2.imread(r'D:\sem_6\IP\OpenCVPract\img7.jpg',0)
k=cv2.imread(r'D:\sem_6\IP\OpenCVPract\1bit1.png',0)
 
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
#o=i+k
#
#plt.title(" ADD Result")
#plt.imshow(cv2.cvtColor(o,cv2.COLOR_BGR2RGB))
#plt.figure()
o=cv2.add(i,k)
plt.title(" CV2 ADD Result")
plt.imshow(cv2.cvtColor(o,cv2.COLOR_BGR2RGB))
plt.figure()
o=cv2.subtract(i,k)
plt.title(" CV2 SUBTRACT Result")
plt.imshow(cv2.cvtColor(o,cv2.COLOR_BGR2RGB))
plt.figure()
o=i*k
plt.title(" Multiply Result")
plt.imshow(cv2.cvtColor(o,cv2.COLOR_BGR2RGB))
plt.figure()
o=cv2.addWeighted(i,0.5,k,0.5,0)
#Add Add Weighted ADD 
plt.title(" Weighted Add Result")
plt.imshow(cv2.cvtColor(o,cv2.COLOR_BGR2RGB))

plt.show()