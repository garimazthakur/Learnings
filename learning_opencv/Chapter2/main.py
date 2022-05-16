# functions required
import cv2
import numpy as np
img= cv2.imread("/home/softuvo/Garima/CNN/Resources/image2.jpeg")
kernel =np.ones((5,5), np.uint8)
imgGray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvtcolor converts the image into  different colors.
imgBlur=cv2.GaussianBlur(imgGray, (3,3), 0)
imgBlur1=cv2.GaussianBlur(imgGray, (7,7), 0)

# edge detector
imgCanny= cv2.Canny(img, 150,200)

# dilaton
imgDilation= cv2.dilate(imgCanny,kernel, iterations=1)

# erosion- make the image thinner
imgEroded= cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blurr Image", imgBlur)
cv2.imshow("Blurr1 Image", imgBlur1)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

