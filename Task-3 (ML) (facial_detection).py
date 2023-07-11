import cv2
cap = cv2.VideoCapture(0)
facemodel = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    status, photo = cap.read()

    coord = facemodel.detectMultiScale(photo)
    

    if len(coord) == 1:
        x1 = coord[0][0]
        y1 = coord[0][1]
        x2 = coord[0][0] + coord[0][2]
        y2 = coord[0][1] + coord[0][3]
        pic = photo[y1:y2,x1:x2]
        cv2.rectangle(photo , (x1,y1) , (x2,y2) , [0,255,0], 5  )
    cv2.imshow("Cropped Image" , pic)
    if cv2.waitKey(10) == 13:
        break
        
cv2.destroyAllWindows()
cap.release()