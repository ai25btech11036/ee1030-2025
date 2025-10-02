import numpy as np
import matplotlib.pyplot as plt

# Matrix A
A = np.array([[-3, 6],
              [-2, 4]])

# Define some vectors to visualize
vectors = [np.array([1, 1]),
           np.array([2, 1]),
           np.array([1, -1]),
           np.array([3, 2])]

# Apply A to each vector
transformed = [A @ v for v in vectors]

# Plot original and transformed vectors
plt.figure(figsize=(6,6))
ax = plt.gca()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')

# Plot original vectors (blue)
for v in vectors:
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.6)

# Plot transformed vectors (red)
for v in transformed:
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='red', alpha=0.6)

# Axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.title("Action of A on vectors (Blue = original, Red = A·v)")
plt.grid(True)
plt.show()