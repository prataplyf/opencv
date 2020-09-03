import cv2
import numpy as np

# in this I'll use erode function that hepls to get the proper edges of an image

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('Resources/githubProfile.jpg')

imgCanny = cv2.Canny(img, 100, 100)
imgDilatation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDilatation, kernel, iterations=1)

cv2.imshow("Dialation Image", imgDilatation)
cv2.imshow("Erode Image", imgErode)

cv2.waitKey(0)
cv2.destroyAllWindows()