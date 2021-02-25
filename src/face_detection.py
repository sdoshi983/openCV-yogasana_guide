import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("../assets/haarcascade_frontalface_default.xml")

while True:
    isReturned, frame = cap.read()
    if isReturned:
        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)

        cv2.imshow('My Face', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()