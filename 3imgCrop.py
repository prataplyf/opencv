# Using OpenCV learn how to crop/reshape the original image
# import library
import cv2
# import image
img = cv2.imread('Resources/githubProfile.jpg')
# to crop/reshape image we'll using matrix formula that contains the initial
# and final coordinates of that image
print(img.shape)
# imgCrop = img[height(y-axis), width(x-axis)]
# height: that contains the initial and final points in y-axis
# width: that contains the initial and final points in x-axis
imgCropped = img[0:200, 0:200]

cv2.imshow("Original", img)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()