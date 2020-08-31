import cv2
import numpy as np

# in this tutorial you will learn that how to get a higher edges of an
# image by increasing the itretation value.

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('Resources/githubProfile.jpg')

imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)

cv2.waitKey(0)
cv2.destroyAllWindows()