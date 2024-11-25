import numpy as np
from sklearn.linear_model import LinearRegression

# Data
y = np.array([32, 47, 18, 25, 49, 41, 52, 38, 36, 29, 43, 28, 24, 36, 41])
x1 = np.array([249, 292, 183, 201, 310, 248, 246, 241, 288, 191, 248, 210, 256, 275, 241])
x2 = np.array([15, 18, 14, 16, 21, 20, 18, 14, 13, 15, 21, 18, 20, 16, 19])

# Prepare data for regression
X = np.column_stack((x1, x2))

# Perform regression
model = LinearRegression()
model.fit(X, y)

# Extract coefficients
beta_0 = model.intercept_
beta_1, beta_2 = model.coef_

print(f"y = {beta_0:.2f} + {beta_1:.2f}x1 + {beta_2:.2f}x2")
