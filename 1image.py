# This is our first program in this we're going to see and analyse that how openCV will read an image from our system/file.
# we need to import cv2 library that will use to give permission to read and show images

# import opencv libraries
import cv2
# to read image in python using opoencv we use cv2.imread() function, here "imread()" function use to read image from file path.
# import images
img = cv2.imread("Resources/githubProfile.jpg")
print(img.shape) # print the shape of image (height and width)

# to show image we use cv2.imshow() function, "imshow()" function is used to show/display image on  screen within the window framework.
# imshow(): this function will create a window framework inside that image will displaying.
# It'll take 2 parameter one for framework name and another is the image like: img
cv2.imshow("githubProfile", img)

# cv2.imshow() will only able to show image but to see image for a perticular period of time we need to use delay function, and this can be done by cv2.waitKey() function.
# cv2.waitKey(): it'll contains only integer value that'll represent that for how many time/second image will stay inside the framework, once the time pass the framework automatic close
cv2.waitKey(0)  # 0(zero) is use to show image for infinite time untill users manually close the framework

