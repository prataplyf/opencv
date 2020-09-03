import cv2
import numpy as np

img = cv2.imread('Resources/card.jpg')
width, height = 150, 250
# [[467, 290], [585, 352], [370, 443], [490, 515]]
# [[270, 305], [382, 367], [171, 465], [285,532]]
""" a1, a2, a3, a4 == [x-axis, y-axis]
    [[a1], [a2], [a3], [a4]]
    a1 ------- a2
    ------------
    ------------
    ------------
    a3 -------- a4
"""

pts1 = np.float32([[467, 290], [585, 352], [370, 443], [490, 515]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)  # source and destination
imgOutput = cv2.warpPerspective(img, matrix, (width, height))



cv2.imshow('Originam Image', img)
cv2.imshow('Warp Image', imgOutput)

cv2.waitKey(0)