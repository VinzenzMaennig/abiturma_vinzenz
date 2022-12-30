import numpy as np

# Define the coefficients of the equations
a = np.array([[2, 2, -2],[1, -1, -2],  [4, 6, 2]])
b = np.array([0, 2, 0])

# Solve the system of equations
x = np.linalg.solve(a, b)

print(x)