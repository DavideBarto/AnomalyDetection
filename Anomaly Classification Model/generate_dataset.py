import numpy as np
import pandas as pd
import random

# Generate normal data
def generate_normal_data(n_points):
    return np.random.normal(loc=25, scale=2, size=n_points)  # Mean 25, Std Dev 2

# Add random noise
def add_random_noise(data, intensity=50):
    noise = data + np.random.normal(loc=0, scale=intensity, size=len(data))
    return noise

# Add gradual drift
def add_gradual_drift(data):
    drift = data + np.linspace(0, 10, len(data))
    return drift

# Add sudden drops
def add_sudden_drops(data, intensity=50):
    drop = data - np.random.uniform(20, intensity, size=len(data))
    return drop

# Create labeled dataset
def create_dataset(n_samples=1000):
    data = []
    labels = []
    for _ in range(n_samples):
        category = random.choice(["normal", "noise", "drift", "drop"])
        if category == "normal":
            readings = generate_normal_data(50)
            label = 0
        elif category == "noise":
            readings = add_random_noise(generate_normal_data(50))
            label = 1
        elif category == "drift":
            readings = add_gradual_drift(generate_normal_data(50))
            label = 2
        elif category == "drop":
            readings = add_sudden_drops(generate_normal_data(50))
            label = 3

        data.append(readings)
        labels.append(label)

    return np.array(data), np.array(labels)
