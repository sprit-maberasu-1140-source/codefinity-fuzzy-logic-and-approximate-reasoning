import numpy as np

temperature_membership = 0.7
humidity_membership = 0.5

# Implement fuzzy AND using the minimum operator
fuzzy_and_result = min(temperature_membership, humidity_membership)

# Implement fuzzy OR using the maximum operator
fuzzy_or_result = max(temperature_membership, humidity_membership)

# Implement fuzzy AND using the product t-norm
fuzzy_and_product = temperature_membership * humidity_membership