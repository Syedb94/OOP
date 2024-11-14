from Shapes3D import Shapes3D
import math
import matplotlib.pyplot as plt
import numpy as np
from math import pi 

class Sphere3(Shapes3D):
    def __init__(self, colour, radius):
        super().__init__("sphere", colour)
        self.radius = radius

    def volume(self):
        return (self.radius ** 3) * (4/3) * math.pi 
    

    def surfacearea(self):
        return 4 * math.pi * (self.radius ** 2)

    def area(self):
        print(f"Drawing a {self.colour} sphere with radius {self.radius}.")
        #return self.circumference * math.pi    

    # draw method
    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = 10 * np.outer(np.cos(u), np.sin(v))
        y = 10 * np.outer(np.sin(u), np.sin(v))
        z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

        # Plot the surface
        ax.plot_surface(x, y, z)

        # Set an equal aspect ratio
        ax.set_aspect('equal')

        plt.show()

sphere = Sphere3("blue", 6.0)  # Create an instance of Sphere3

# Round the volume and surface area
volume = round(sphere.volume(), 1)
surface_area = round(sphere.surfacearea(), 1)



# Define the radius of the sphere
r = 6.0

# Calculate the volume of the sphere using the formula
V = 4.0/3.0 * pi * r**3
