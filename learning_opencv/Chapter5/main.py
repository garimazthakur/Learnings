# WRAP PERSPECTIVE

import cv2
import numpy as np
height, width = 250, 350
img=cv2.imread("/home/softuvo/Garima/learning_opencv/Resources/cards.jpg")
pts1= np.float32([[111,219], [287,188], [154,482], [352,440]])
pts2=np.float32([[0,0], [width,0], [0,height], [width, height]])
matrix= cv2.getPerspectiveTransform(pts1, pts2)
imageOutput=cv2.warpPerspective(img, matrix,(width, height))

cv2.imshow("image", img)
cv2.imshow("Output", imageOutput)

cv2.waitKey(0)