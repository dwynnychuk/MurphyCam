import cv2

# access camera and display image. ESC key to stop
cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()