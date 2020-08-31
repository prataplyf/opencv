import cv2

# In this tutorial, you will learn how to blur images.
# read images
img = cv2.imread('Resources/githubProfile.jpg')

# apply a Gaussian blur to the input image using our computed
# kernel size
imgBlur = cv2.GaussianBlur(img, (7,7), 0)

cv2.imshow("Color Image", img)
cv2.imshow("Blur Image", imgBlur)
# cv2.imwrite('Resources/github.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()

