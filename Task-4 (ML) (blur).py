import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

while True:
    ret, photo = video_capture.read()
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = photo[y:y+h, x:x+w]
        blurred_photo = cv2.GaussianBlur(photo, (25, 25), 0)
        blurred_photo[y:y+h, x:x+w] = face_roi
        cv2.imshow('Result', blurred_photo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
