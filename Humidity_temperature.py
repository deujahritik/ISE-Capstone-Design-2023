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
