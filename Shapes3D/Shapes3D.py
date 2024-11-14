
#Super

class Shapes3D():
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

    def gettype(self):
        return self.type

    def getcolour(self):
        return self.colour

    def settype(self, new_type):
        self.type = new_type

    def setcolour(self, colour):
        self.colour = colour

    def volume(self):
        pass

    def surfacearea(self):
        pass

    def draw(self):
        print(f"Drawing a {self.type} in colour {self.colour}.")
        





