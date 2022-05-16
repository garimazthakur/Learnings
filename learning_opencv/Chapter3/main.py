import cv2
img=cv2.imread("/home/softuvo/Garima/CNN/Resources/tesla.jpg")
print(img.shape)

# resize image
imgResize=cv2.resize(img,(600,300))
print(imgResize.shape)


# crop an image
imgCropped = img[0:500,500:900] 

cv2.imshow("image", img)
cv2.imshow("imageResized", imgResize)
cv2.imshow("imageCropped", imgCropped)


cv2.waitKey(0)



