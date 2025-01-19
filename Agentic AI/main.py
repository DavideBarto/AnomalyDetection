from sensor import Sensor
import random
from utility import inject_anomaly
from agent import agent_monitor

sensor_network = [Sensor(f"{i}") for i in range(10)]
# Inject anomalies into random sensors
for _ in range(2):
    inject_anomaly(random.choice(sensor_network))

# Run the agent
agent_monitor(sensor_network)

