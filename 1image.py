# import opencv libraries
import cv2

# import images
img = cv2.imread("Resources/githubProfile.jpg")
print(img.shape)
cv2.imshow("githubProfile", img)
cv2.waitKey(0)

