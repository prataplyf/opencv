import cv2

cap_vid = cv2.VideoCapture("Resources/video.mp4")

while True:
    success, img = cap_vid.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        pass