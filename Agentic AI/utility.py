import random

def inject_anomaly(sensor):
    # Simulate an anomaly by introducing a large deviation
    sensor.reading += random.uniform(50.0, 100.0)

def detect_anomalies(sensor_network):
    readings = [sensor.reading for sensor in sensor_network if sensor.status == "active"]
    mean = sum(readings) / len(readings)
    std_dev = (sum((x - mean) ** 2 for x in readings) / len(readings)) ** 0.5
    threshold = mean + 3 * std_dev

    anomalies = []
    for sensor in sensor_network:
        if sensor.reading > threshold:
            anomalies.append(sensor)
    return anomalies

