from cubeClass import Cube
from sphere import Sphere3
import turtle


# creating objects to test
aSphere = Sphere3("blue" ,10)
aCube = Cube("yellow", 5)
print("Colour of Sphere =", aSphere.getcolour())
print("Volumn of Sphere=", round(aSphere.volume(), -1))
print("Surface area of sphere:", round(aSphere.surfacearea(), -1))

aSphere.draw()

# aSphere.draw()


print("Cube's Color:", aCube.getcolour())
print("Cube's Volume:", aCube.volume())
print("Cube's Surface Area:", aCube.surfacearea())
aCube.draw()
