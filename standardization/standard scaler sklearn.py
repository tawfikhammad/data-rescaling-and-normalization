from sklearn.preprocessing import StandardScaler
import numpy as np

# Generate example data
data = np.random.rand(100, 3)  # A 2D array with 100 samples and 3 features

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the data and transform the data
standardized_data = scaler.fit_transform(data)

# Print the standardized data
print("Standardized Data:")
print(standardized_data)