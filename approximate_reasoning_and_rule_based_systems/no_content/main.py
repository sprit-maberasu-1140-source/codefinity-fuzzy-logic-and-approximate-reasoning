import numpy as np

# Membership functions for temperature
def temp_cool(x):
    return max(0, min(1, (25 - x) / 10))

def temp_hot(x):
    return max(0, min(1, (x - 20) / 10))

# Membership functions for humidity
def hum_dry(x):
    return max(0, min(1, (60 - x) / 30))

def hum_humid(x):
    return max(0, min(1, (x - 40) / 30))

# Membership functions for fan speed
def speed_low(x):
    return max(0, min(1, (50 - x) / 30))

def speed_high(x):
    return max(0, min(1, (x - 30) / 30))

# Crisp inputs
temperature = 28
humidity = 65

# Fuzzification
temp_cool_val = temp_cool(temperature)
temp_hot_val = temp_hot(temperature)
hum_dry_val = hum_dry(humidity)
hum_humid_val = hum_humid(humidity)

# Rule evaluation
rule1_strength = max(temp_hot_val, hum_humid_val)
rule2_strength = min(temp_cool_val, hum_dry_val)

# Aggregation and defuzzification
x_range = np.linspace(0, 80, 100)
aggregated = np.zeros_like(x_range)

for i, x in enumerate(x_range):
    high_val = min(rule1_strength, speed_high(x))
    low_val = min(rule2_strength, speed_low(x))
    aggregated[i] = max(high_val, low_val)

fan_speed = 0 if np.sum(aggregated) == 0 else np.sum(x_range * aggregated) / np.sum(aggregated)