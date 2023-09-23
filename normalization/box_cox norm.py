import numpy as np
from scipy import stats

# Generate example data (positively skewed)
data = np.random.exponential(scale=2, size=100)

# Apply Box-Cox transformation
transformed_data, lambda_ = stats.boxcox(data)

# Print the transformed data and estimated lambda
print("Transformed Data:", transformed_data)
print("Estimated Lambda:", lambda_)
