# Using OpenCV learn how to Resize the original image
# import libraries
import cv2
# import image
img = cv2.imread('Resources/githubProfile.jpg')
# to resize image we need image, resize_width and resize_height
# openCV contains width first then it call height
# while simple matrix occour height first and then width
# imgResize = cv2.resize(original image, (width, height))
imgResize = cv2.resize(img, (200,300))

cv2.imshow("Original", img)
cv2.imshow("Resize", imgResize)

cv2.waitKey(0)
cv2.destroyAllWindows()