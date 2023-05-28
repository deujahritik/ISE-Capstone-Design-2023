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
 

