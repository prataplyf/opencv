import cv2
import numpy as np

# In this tutorial, you will learn how to convert images from one color-space to another,
# like BGR \leftrightarrow Gray, BGR \leftrightarrow HSV etc.
# cv2. cvtColor() method is used to convert an image from one color space to another.
# There are more than 150 color-space conversion methods available in OpenCV.

# reading images from source
img = cv2.imread('Resources/githubProfile.jpg')

"""
    # To get all 150 color List
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print(flags)
"""

# converting colored image into grey color
# For color conversion, we use the function cv2.cvtColor(input_image, flag) where flag determines the type of conversion.
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# lower_blue = np.array([110,50,50])
# upper_blue = np.array([130,255,255])
# # Threshold the real image to get only blue colors
# mask = cv2.inRange(img, lower_blue, upper_blue)

# # Bitwise-AND mask and original image
# res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow("Color Image", img)
cv2.imshow("Grey Image", imgGrey)
# cv2.imshow("Mask", mask)
# cv2.imshow("Response", res)

# cv2.imshow() will only able to show image but to see image for a perticular period of time we need to use delay function, and this can be done by cv2.waitKey() function.
# cv2.waitKey(): it'll contains only integer value that'll represent that for how many time/second image will stay inside the framework, once the time pass the framework automatic close
cv2.waitKey(0)  # 0(zero) is use to show image for infinite time untill users manually close the framework

# Destroy all opened windows
cv2.destroyAllWindows()