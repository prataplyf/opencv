import cv2
import numpy as np
img = cv2.imread("Resources/githubProfile.jpg")

imgHor = np.hstack((img,img))
img = cv2.resize(img, (200,200))
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)


cv2.waitKey(0)



