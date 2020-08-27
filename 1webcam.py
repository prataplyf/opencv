# This is our third program in this we're going to see and analyse that how openCV will read a webcam.
# we need to import cv2 library that will use to give permission to read and show images

# import opencv libraries
import cv2

# to read webcam video image in python, we use opoencv cv2.VideoCapture() function, here "VideoCapture()" function use to read image from webcam.
# capture video
cap_vid = cv2.VideoCapture(0) # to read video images from webcam we ID of that webcam, like what is the ID of a particular webcam
cap_vid.set(3, 640) # ID and height
cap_vid.set(4, 480) # ID and width
cap_vid.set(10,100) # ID and brightness

# video is a combination of images so we are going to get all images of video and display one-by-one that'll looks like a real video
while True:
    # we need to use 2 parameter that tell is the image is successfully read or not and the second pamareter use to read the image
    # here "success" parameter will be show a boolean value that inform us that image successfully read ot not
    # img variable is used to read and store video images
    success, img = cap_vid.read()
    # to show image we use cv2.imshow() function, "imshow()" function is used to show/display image on  screen within the window framework.
    # imshow(): this function will create a window framework inside that image will displaying.
    # It'll take 2 parameter one for framework name and another is the image like: img
    cv2.imshow("Video", img)
    # cv2.imshow() will only able to show image but to see image for a perticular period of time we need to use delay function, and this can be done by cv2.waitKey() function.
    # cv2.waitKey(): it'll contains only integer value that'll represent that for how many time/second image will stay inside the framework, once the time pass the framework automatic close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # here we use 2 condition first use to display each image for a milisecond and second condition is use to quit video when user pree the "q" button.
        break
    # else:
    #     pass