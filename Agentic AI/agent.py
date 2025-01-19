from utility import detect_anomalies
def agent_monitor(sensor_network):
    while True:
        # Update sensor readings
        for sensor in sensor_network:
            if sensor.status == "active":
                sensor.update_reading()

        # Detect anomalies
        anomalies = detect_anomalies(sensor_network)

        # Handle anomalies
        for sensor in anomalies:
            sensor.status = "inactive"
            print(f"Sensor {sensor.sensor_id} deactivated due to anomaly. Reading: {sensor.reading}")

        # Display current status
        active_sensors = [sensor for sensor in sensor_network if sensor.status == "active"]
        print(f"Active sensors: {[sensor.sensor_id for sensor in active_sensors]}")

        # Stop after one iteration for simplicity in testing
        break
