from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Example data
data = np.array([[2, 5, 13, 20], [10, 8, 3, 15], [4, 0, 30, 12]])

# Create an instance of MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler to the data and transform the data
scaled_data = scaler.fit_transform(data)

# Print the scaled data
print(scaled_data)

