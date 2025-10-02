import matplotlib.pyplot as plt
import numpy as np

# Define the circle (x-1)^2 + y^2 = 1
theta = np.linspace(0, 2*np.pi, 400)
circle_x = 1 + np.cos(theta)
circle_y = np.sin(theta)

# Define the locus circle x^2 + y^2 = x -> (x-0.5)^2 + y^2 = 0.25
locus_x = 0.5 + 0.5*np.cos(theta)
locus_y = 0.5*np.sin(theta)

# Plot
plt.figure(figsize=(6,6))
plt.plot(circle_x, circle_y, label="Original Circle (x-1)^2 + y^2 = 1", color="blue")
plt.plot(locus_x, locus_y, label="Locus of Midpoints x^2 + y^2 = x", color="red")

# Mark origin
plt.scatter(0,0, color="black", s=50, label="Origin (0,0)")

# A sample chord from origin to circle
x_chord = [0, 2*0.5]  # midpoint at (0.5,0)
y_chord = [0, 2*0]
plt.plot(x_chord, y_chord, 'g--', label="Sample Chord")

# Formatting
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Chords from Origin and Locus of Midpoints")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()