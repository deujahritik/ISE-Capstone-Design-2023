###  Here's the  code that uses the webcam (camera) as the video source and allows us to exit the program by pressing the 'Esc' key:

```
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
```
### Screenshots:
![image](https://github.com/deujahritik/ISE-Capstone-Design-2023/assets/92029196/8e5fcb8d-323c-4fa4-a29d-f08988c38fc5)

![image](https://github.com/deujahritik/ISE-Capstone-Design-2023/assets/92029196/a5c84d5e-0adf-4afb-b4ed-88f540123df8)

