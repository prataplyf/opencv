import cv2

cap_vid = cv2.VideoCapture(0)
cap_vid.set(3, 640)
cap_vid.set(4, 480)
cap_vid.set(10,100)

while True:
    success, img = cap_vid.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # else:
    #     pass