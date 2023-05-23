import RPi.GPIO as GPIO
import time

# GPIO pin connected to the moisture sensor
moisture_pin = 14

# GPIO pins connected to the water pump
pump_pin = 15

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(moisture_pin, GPIO.IN)
GPIO.setup(pump_pin, GPIO.OUT)

# Define threshold moisture level
threshold_moisture = 500  # Adjust this value according to your sensor's readings

# Function to control the water pump
def control_water_pump(pump_status):
    GPIO.output(pump_pin, pump_status)

try:
    while True:
        # Read moisture level
        moisture_level = GPIO.input(moisture_pin)

        if moisture_level < threshold_moisture:
            print("Moisture level is low. Pumping water.")
            control_water_pump(GPIO.HIGH)  # Turn on the water pump
        else:
            print("Moisture level is sufficient.")

        time.sleep(1)  # Wait for 1 second before checking again

except KeyboardInterrupt:
    GPIO.cleanup()
