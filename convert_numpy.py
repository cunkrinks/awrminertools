import numpy as np

# Example multi-dimensional NumPy array with mixed data types
data = np.array([
    ['10', 'hello', '20'],
    ['30', 'world', '40'],
    ['50', '60', 'text']
])

# Create an empty array to store the converted data
#converted_data = np.zeros_like(data, dtype=object) # Use object dtype to allow mixed types
converted_data = np.empty(shape=data.shape, dtype=object)  # Use object dtype to allow mixed types

# Iterate through the array and convert numeric strings to integers
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        try:
            # Attempt to convert the element to an integer
            converted_data[i, j] = int(data[i, j])
        except ValueError:
            # If conversion fails (e.g., it's not a valid number), keep the original value
            converted_data[i, j] = data[i, j].strip()

print("Original Array:")
print(data)
print("\nConverted Array:")
print(converted_data)