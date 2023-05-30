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

### Overview
*This system is designed to monitor and manage the environmental conditions essential for plant growth, such as moisture, humidity, and temperature. One of its smart features is the ability to intelligently irrigate your plants based on real-time moisture level data. Furthermore, it includes a webcam for people detection, distinguishing authorized from unauthorized individuals. All sensor data is stored in a JSON file, which can be uploaded to the cloud and accessed for further usage.*

### Key features
***1.Smart Irrigation:***
*The system continuously monitors soil moisture levels and activates the water pump to irrigate plants when the soil moisture level is low. This ensures that plants are watered efficiently and precisely when they need it.
***2.Environmental Monitoring:***
*In addition to soil moisture, the system also monitors and records the temperature and humidity in the environment.*
***3.People Detection:***
*The webcam identifies authorized and unauthorized individuals, contributing to the security of the system.*
***4.Data Storing and Sharing:***
*All collected data are stored in a JSON file and can be uploaded to the cloud for access from the web or other applications.*

### Advantages Over Existing Systems
*•Intelligent Irrigation: Unlike traditional systems which irrigate on a set schedule, the Smart Plant Caring System adjusts irrigation based on real-time soil moisture levels, resulting in more efficient water usage and healthier plants. *

*•Integrated Monitoring: The system monitors multiple factors (soil moisture, temperature, humidity), providing a comprehensive understanding of the plant's environment.*

*•Security Feature: The inclusion of people detection adds a layer of security not commonly found in traditional plant caring systems.*

*•Cloud Compatibility: The ability to upload data to the cloud makes it easy to monitor and analyze your plant's environment from anywhere, at any time.*

### Who can use it?
*This system is ideal for indoor garden enthusiasts, smart home hobbyists, and those looking to implement an automated plant care solution at home, in an office, or any indoor setting. It is also a great learning tool for students and researchers in the fields of IoT and automation.*

### Why It Is Useful?
*The Smart Plant Caring System simplifies and optimizes the process of indoor plant care. It provides real-time monitoring and smart control, relieving you from the routine of manual watering and enabling more efficient plant care. By detecting people, the system also adds an extra layer of security. The data storage and sharing capability offer valuable insights into your plant's growth pattern and environmental requirements.*

### Hardware Used

* Raspberry Pi 3 

* Webcam 

* humidity and temperature sensor 

* Moisture sensor 

* Water pump 9V power supply Plants 

# Codes
## Humidity_temp.py

```python
import os
import json
import time
import board
import adafruit_dht

# Initialize the DHT device with data pin connected to GPIO pin 17 (change if necessary)
dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)

# Create the folder to store JSON data if it doesn't exist
data_folder = "JSON_Humidity_Temperature_data"
os.makedirs(data_folder, exist_ok=True)

# File to store the sensor data
filename = f"{data_folder}/sensor_data.txt"

while True:
    try:
        # Read the humidity and temperature values from the sensor
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

        # Create a dictionary with the sensor data
        sensor_data = {
            "timestamp": str(time.time()),
            "temperature_c": temperature_c,
            "temperature_f": temperature_f,
            "humidity": humidity
        }
            # Append the new data to the file
        with open(filename, "a") as file:
            file.write(json.dumps(sensor_data) + "\n")

    except RuntimeError as error:
        # Errors happen fairly often, DHT sensors can be hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue

    time.sleep(2.0)
    
  ```
  
  ## Moisture_sensor.py
  
  ```python
  # Create an empty list to store pump status data
pump_status_list = []

# Initialize the pump status
pump_status = "off"

while True:
    moisture_level = moisture_sensor.value * 100
    print(f"Moisture level: {moisture_level:.2f}%")

    if moisture_level < moisture_threshold:
        #print('Moisture level is low. Watering the plant...')
        print('Moisture level is sufficient.')
        water_pump.on()  # Turn on the water pump
        pump_status = "on"
        time.sleep(5)  # Run the water pump for 5 seconds
        water_pump.off()  # Turn off the water pump
        print('Watering complete.')
    else:
        #print('Moisture level is sufficient.')
        print('Moisture level is low. Watering the plant...')
        pump_status = "off"

    # Get the current timestamp
    current_time = str(datetime.now())

    # Create a dictionary with the pump status data
    pump_status_data = {
        "time": current_time,
        "status": pump_status
    }

    # Append the pump status data to the list
    pump_status_list.append(pump_status_data)

    # Generate a filename for the JSON file
    filename = f"{data_folder}/pump_status.json"

    # Save all pump status data to a JSON file in column and row format
    with open(filename, "w") as file:
        json.dump(pump_status_list, file, indent=4)

    time.sleep(2)
    
    ```
 

```
# Implementng face detection system
## Step 1: Setting up the Raspberry Pi
We will begin by setting up the Raspberry Pi. Follow the instructions given in the Raspberry Pi Setup Guide to set up your Raspberry Pi. https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up

## Step 2: Installing OpenCV on Raspberry Pi

The next step is to install OpenCV on the Raspberry Pi. We will use the pre-built OpenCV package provided by the Raspberry Pi community.

1. Open the terminal on your Raspberry Pi and run the following command to update the package list:
sql
```python
sudo apt-get update
```
2. Install OpenCV by running the following command:
arduino
```python
sudo apt-get install libopencv-dev python3-opencv
```
3. Verify the installation by running the following command:
scss
```python
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
```python
import cv2
import numpy as np
```
3. Load the trained face detection model:
python
```python
face_cascade = cv2.CascadeClassifier('path/to/haar/cascade/xml/file')
```
4. Initialize the video stream from the Raspberry Pi camera module:
python
```python
cap = cv2.VideoCapture(0)
```
5. Start the main loop to capture and process the video frames:
python
```python
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
