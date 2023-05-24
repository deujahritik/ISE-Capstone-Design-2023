# ISE-Capstone-Design-2023
##  IoT in Agriculture: Smart Plant Care System (Automation & Monitoring)
## TEAM 6
```
ISE:
12194824 Ritik Deuja
12200306 Asadbek Khoshmov
12200311Azizbek Akhmadov
IBT:
12200334 Jaloliddin Abdullajonov
12194938 Babina Tamang
12194927 Jasurbek Tulkinhujaev
12184750 Ulugbek Oripov
12200341 Shokhrukh Khayitov
```
## Project Prototype:
![image](https://github.com/deujahritik/ISE-Capstone-Design-2023/assets/92029196/028fa211-2644-4dea-a419-bac87fcfb2d3)

## Main Function
*When it comes project functions,*

### In security part:

*•It can detect authorized and unauthorized people*

*•It can count entered people into green house.*

*•It can do face recognition.*

*• Save data in cloud.*


### In watering part:

*•It can detect moisture of the soil.*

*•It pumps water.*

*•It can detect humidity and temperature.*

*•It can also monitor plant’s health.*

*•It can take real time video.*

# Implementng face detection system
## Step 1: Setting up the Raspberry Pi
We will begin by setting up the Raspberry Pi. Follow the instructions given in the Raspberry Pi Setup Guide to set up your Raspberry Pi. https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up

## Step 2: Installing OpenCV on Raspberry Pi

The next step is to install OpenCV on the Raspberry Pi. We will use the pre-built OpenCV package provided by the Raspberry Pi community.

1. Open the terminal on your Raspberry Pi and run the following command to update the package list:
sql
```
sudo apt-get update
```
2. Install OpenCV by running the following command:
arduino
```
sudo apt-get install libopencv-dev python3-opencv
```
3. Verify the installation by running the following command:
scss
```
python3 -c "import cv2;print(cv2.__version__)"
```
If the installation is successful, you should see the version of OpenCV printed on the screen.

## Step 3: Collecting Dataset and Preparing it for Training

For this demo, we will use the Labeled Faces in the Wild (LFW) dataset, which contains images of faces with corresponding labels. Download the dataset from the official website and extract it to a local folder.

Next, we need to prepare the dataset for training the face detection model. We will use the Cascade Trainer GUI tool to train the face detection model.

1. Download the Cascade Trainer GUI tool from the official website and extract it to a local folder.

2. Open the tool and click on the "Create a New Project" button.

3. Fill in the project details and click on the "Create" button.

4. Click on the "Add Images" button and select the images from the LFW dataset.

Click on the "Add Annotations" button and manually annotate the faces in the images.

5. Click on the "Train Cascade" button and follow the instructions to train the face detection model.

6. Once the training is complete, export the model to a local folder.

## Step 4: Implementing the Face Detection System

Now that we have trained the face detection model, we can implement the real-time face detection system using Raspberry Pi and OpenCV.

1. Connect the Raspberry Pi camera module to the Raspberry Pi.

2. Create a new Python file and import the necessary libraries:

python
```
import cv2
import numpy as np
```
3. Load the trained face detection model:
python
```
face_cascade = cv2.CascadeClassifier('path/to/haar/cascade/xml/file')
```
4. Initialize the video stream from the Raspberry Pi camera module:
python
```
cap = cv2.VideoCapture(0)
```
5. Start the main loop to capture and process the video frames:
python
```
while True:
    # Read the video frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the video frame
    cv2
    ```
