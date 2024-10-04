import numpy as np
from matplotlib import pyplot as plt
import cv2

#read the image
img=cv2.imread("J:\5th sem\Python\Code Unati\image15-6.png",0)

plt.subplot(231)
plt.title(" Histogram of Original Image")
plt.hist(img.ravel(),bins=255,range=(1,img.ravel().max()))

plt.subplot(234)
plt.title("Original Image ")
plt.imshow(img,cmap='gray')

#find max
max_img=np.max(img)
print("Max of img :",max_img)

# find min
min_img=np.min(img)
print("Min of img :",min_img)

#calculate bins value
bins=max_img-min_img
print("Value of bins :",bins)

#find total number of pixels from histogram
h=np.histogram(img,bins,(min_img,max_img))[0]
print("No of pixels :",h)

#apply min-max stretch
str_img=255*((img-min_img)/(max_img-min_img))

plt.subplot(232)
plt.title("Histogram of Stretched Image ")
plt.hist(str_img.ravel(),bins=255,range=(1,str_img.ravel().max()))

plt.subplot(235)
plt.title("Stretched Image ")
plt.imshow(str_img,cmap='gray')

#To find tL and tU
tL=np.percentile(str_img,1).astype(int)
tU=np.percentile(str_img,99).astype(int)
print("Lower threshold :",tL)
print("Upper threshold :",tU)

#apply percentile stretch
#find points below threshold value
below_tL = np.asarray(str_img < tL)

str_img[below_tL] = tL

print("points below lower threshold:",str_img)

#find points above the upper threshold
above_tU = np.asarray(str_img > tU)

str_img[above_tU] = tU

print("points above upper threshold:",str_img)

#set pixels between tL and tU values
str_img=((str_img-tL)/(tU-tL))*255
print("percentile stretch image :",str_img)

#plot subgraphs of images and histograms

plt.subplot(233)
plt.title(" Histogram of Saturated contrast stretch Image")
plt.hist(str_img.ravel(),bins=255,range=(1,str_img.ravel().max()))

plt.subplot(236)
plt.title("Percentile Stretched Image ")
plt.imshow(str_img,cmap='gray')
