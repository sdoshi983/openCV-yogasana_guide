import cv2

cap = cv2.VideoCapture(0)

while True:
    isReturned, frame = cap.read()
    if isReturned:
        cv2.imshow('My Face', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cap.release()