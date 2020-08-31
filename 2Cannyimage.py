import cv2
# In this tutorial, you will learn how to detect the edges of image.
img = cv2.imread('Resources/githubProfile.jpg')

# cv2.canny(img, thr1, thr2)
# this function contains 2 thresheld function one is upper threshold and lower threshold value
imgCanny = cv2.Canny(img, 100, 100)

cv2.imshow("Color Image", img)
cv2.imshow("Canny Image", imgCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()