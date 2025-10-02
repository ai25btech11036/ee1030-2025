import matplotlib.pyplot as plt
import numpy as np

# Parameters of the ellipse
a = 4  # semi-major axis (half-width)
b = 2  # semi-minor axis (height)

# Semi-ellipse (upper half)
x = np.linspace(-a, a, 400)
y = b * np.sqrt(1 - (x*2 / a*2))

# Point 1.5 m from left end (x = -4 + 1.5 = -2.5)
x_point = -2.5
y_point = b * np.sqrt(1 - (x_point*2 / a*2))

# Plot
plt.figure(figsize=(7,4))
plt.plot(x, y, label="Arch (Semi-Ellipse)", color="blue")
plt.scatter(x_point, y_point, color="red", s=60, label=f"Point 1.5 m from end\n({x_point:.1f}, {y_point:.3f})")

# Mark ends and center
plt.scatter([-a, 0, a], [0, b, 0], color="black", s=40)
plt.text(-a, -0.2, "(-4,0)", ha="center")
plt.text(a, -0.2, "(4,0)", ha="center")
plt.text(0, b+0.2, "(0,2)", ha="center")

# Formatting
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Semi-Elliptical Arch (2D Diagram)")
plt.xlabel("Width (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()