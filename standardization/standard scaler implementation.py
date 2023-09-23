import numpy as np

def standardize(X):
  
  # Calculate the mean and standard deviation of each feature.
  mean = np.mean(X, axis=0)
  std = np.std(X, axis=0)

  # Subtract the mean and divide by the standard deviation for each feature.
  X_std = (X - mean) / std

  return X_std

data = np.random.rand(100, 3)  # A 2D array with 100 samples and 3 features

X_std = standardize(data)
print(X_std)
