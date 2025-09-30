import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Example values of alpha and beta (you can change them)
alpha, beta = 2, 3  

# Define vectors OP, OQ, OR
OP = np.array([(alpha - 1) / alpha, 1, 1])
OQ = np.array([1, (beta - 1) / beta, 1])
OR = np.array([1, 1, 0.5])

# Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot origin
ax.scatter(0, 0, 0, color='k', s=50)

# Plot vectors from origin
ax.quiver(0, 0, 0, *OP, color='r', label='OP')
ax.quiver(0, 0, 0, *OQ, color='g', label='OQ')
ax.quiver(0, 0, 0, *OR, color='b', label='OR')

# Plane: 3x + 3y - z + l = 0
# Find l so that (alpha, beta, 2) lies on it
l = -(3*alpha + 3*beta - 2)

# Create meshgrid for plane
xx, yy = np.meshgrid(np.linspace(-1, 3, 10), np.linspace(-1, 3, 10))
zz = 3*xx + 3*yy + l

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
ax.set_title("3D Plot of Vectors OP, OQ, OR and Plane")

plt.show()