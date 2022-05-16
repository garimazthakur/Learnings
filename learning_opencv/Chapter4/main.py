# Shapes and Texts
from pickletools import uint8
import cv2
import numpy as np

img= np.zeros((512,512,3), np.uint8)
print(img)

# img[:207]= 255,0,0
# img[207:]= 100,0,0
# img[200:300]= 255,0,0
img[:]= 255,0,0

# cv2.line(img, (0,0), (300,300), (0,255,0),3)
# line(imag, start, end, color, thickness)
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0),3)
cv2.rectangle(img, (0,0), (250,350), (0,0,255),2)  #use cv2.FILLED to fill the rectangle insteasd of  thickness 
# rectangle(imae, define points, define ending points(corner/diagonal point), color, thickness)
cv2.circle(img, (400,50), 30, (255,255,0), 5)

# put text to a function
cv2.putText(img, "OPENCV ", (300,100), cv2.FONT_HERSHEY_COMPLEX, .5,(0,150,0),1) # (img, text, start, font of text,scale of text, color, thickness)

cv2.imshow("image", img)

cv2.waitKey(0)
