# Using OpenCV learn how to write text on the original image
# import library
import cv2
import numpy as np
# import image
img = np.zeros((512,512))

# cv2.putText(img, "Ashish Pratap Singh", (20,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (90,170,90), thickness=2, lineType=1,bottomLeftOrigin=1)
cv2.putText(img, "SHAPES & TEXTS", (100,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (25,25,90), thickness=2)
cv2.imshow("Original", img)
# cv2.putText() have contains several parameters:
# img: image on which putting text
# "SHAPES & TEXTS": the text that you want to put on your image
# (width, height): define the coordinators from where text should be starting to put
# FONT_SIZE: select the font size of text, cv2 has some particular defined shapes
# Sacling: this will contains the both flot and int value for scaling the image
# (25,25,90): color code of text
# thickness: choose the thickness of text, this should be integer not float
cv2.waitKey(0)
cv2.destroyAllWindows()