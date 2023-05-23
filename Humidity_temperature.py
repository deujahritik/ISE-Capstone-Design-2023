import Adafruit_DHT
import time

# Sensor model (DHT11 or DHT22)
sensor = Adafruit_DHT.DHT22

# GPIO pin connected to the sensor data pin
sensor_pin = 4

try:
    while True:
        # Read humidity and temperature from the sensor
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        if humidity is not None and temperature is not None:
            print("Temperature: {:.1f}°C".format(temperature))
            print("Humidity: {:.1f}%".format(humidity))
        else:
            print("Failed to retrieve data from the sensor.")

        time.sleep(2)  # Wait for 2 seconds before reading again

except KeyboardInterrupt:
    pass
