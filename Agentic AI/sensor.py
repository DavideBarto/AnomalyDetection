import random
class Sensor:
    def __init__(self, sensor_id: str):
        #Simulate temperature sensor
        self.reading = random.uniform(20.0, 30.0)
        self.sensor_id = sensor_id
        self.status = "active"

    def update_reading(self):
        # Simulate normal sensor behavior with slight fluctuations
        self.reading += random.uniform(-0.5, 0.5)


