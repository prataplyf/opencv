import cv2
import numpy as np

def stackedImages(scale, imgArray):
    rows = len(imgArray)
    print("Rows:", rows)
    cols = len(imgArray[0])
    print('cols:',cols)
    width = imgArray[0][0].shape[1]
    print('width:',width)
    height = imgArray[0][0].shape[0]
    print('height:',height)
    imageBlank = np.zeros((height, width, 10), np.uint8)
    # print('imageBlank:', imageBlank)
    hor = [imageBlank] * rows
    # print('hor:',hor)
    for x in range(0, rows):
        hor[x] = np.hstack(imgArray[x])
    ver = np.vstack(hor)
    return ver

img = cv2.imread('Resources/wall.jfif')
img = cv2.resize(img, (200,200))
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = [img,img,img]
imgstack = stackedImages(0.5, (img, img, img))
# imgstack = stackedImages(0.5, ([img,img,img]))
cv2.imshow("Stacked Images", imgstack)
cv2.waitKey(0)