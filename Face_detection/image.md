
### The code  is using the OpenCV library (cv2) to perform face detection in an image using the Haar cascade classifier.
```
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()
```

### Screenshot:
![image](https://github.com/deujahritik/ISE-Capstone-Design-2023/assets/92029196/cfe94914-f5ef-4dd4-a194-7d28369a71e7)
![image](https://github.com/deujahritik/ISE-Capstone-Design-2023/assets/92029196/46ff3f8e-2745-4054-9bf5-a299035677f7)

