import cv2 
print("package imported")
#**************************************Reading an Image**************************************
# img=cv2.imread(r"/home/softuvo/Garima/CNN/Resources/image1.png")
# print(img.shape)
# cv2.imshow("output", img)
# cv2.waitKey(0)   #to check the image


#**************************************Video capture image**************************************
# cap = cv2.VideoCapture("/home/softuvo/Garima/CNN/Resources/test_video.mp4")
# while True:
#     success, img= cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


#**************************************live feed from the web camera**************************************
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img= cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# using a webcam




