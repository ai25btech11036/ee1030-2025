import matplotlib.pyplot as plt
import numpy as np

# Define x range
x = np.linspace(-1, 5, 400)

# Equation 1: 7x + 2y = 11  -> y = (11 - 7x)/2
y1 = (11 - 7*x)/2

# Equation 2: 4x - y = 2  -> y = 4x - 2
y2 = 4*x - 2

# Plot the lines
plt.figure(figsize=(6,6))
plt.plot(x, y1, label="7x + 2y = 11")
plt.plot(x, y2, label="4x - y = 2")

# Mark the solution point (1,2)
plt.scatter(1, 2, color="red", zorder=5)
plt.text(1.1, 2.1, "(1,2)", fontsize=12, color="red")

# Axis settings
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("2D Plot of the System of Equations")

plt.show()