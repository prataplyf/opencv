# Using OpenCV learn how to draw line/rectangle/circle on the original image
# import library
import cv2
import numpy as np
# import image
img = np.zeros((512,512))

# putText
cv2.putText(img, "SHAPES & TEXTS", (100,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (25,25,90), thickness=2)
# cv2.putText() have contains several parameters:
# img: image on which putting text
# "SHAPES & TEXTS": the text that you want to put on your image
# (width, height): define the coordinators from where text should be starting to put
# FONT_SIZE: select the font size of text, cv2 has some particular defined shapes
# Sacling: this will contains the both flot and int value for scaling the image
# (25,25,90): color code of text
# thickness: choose the thickness of text, this should be integer not float

# Draw Line
cv2.line(img, (20,70), (492,70), (25,25,90), thickness=3)
# cv2.line()
# img: on that draw line
# start point: it contains width, height of the image
# end point: it contains width, height of the image
# color: color code of the line
# thickness: choose thickness of line this should be int

# Draw Rectangle
cv2.rectangle(img, (40,100), (400,300), (164,255,255), thickness=2)
# cv2.rectangle()
# img: on that draw rectangle
# start point: it contains width, height of the image
# end point: it contains width, height of the image
# color: color code of the line
# thickness: choose thickness of rectangle this should be int

# Draw Circle
cv2.circle(img, (200, 400), 50, (255,190,131), thickness=3)
# cv2.circle()
# img: on that draw circle
# start point: it contains the center point from that it should start creating circle
# radius: define the radius of the circle
# color: color code of the circle
# thickness: choose thickness of circle this should be int

# print image
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()