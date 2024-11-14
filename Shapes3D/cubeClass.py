from Shapes3D import Shapes3D
import turtle

class Cube(Shapes3D):
    def __init__(self, colour, length):
        super().__init__("cube", colour)
        self.length = length
        

    def volume(self):
        return self.length ** 3
    
    def surfacearea(self):
        return 6 * (self.length ** 2)


    #def surfacearea(self):
     #   return self.height * self.length 

    def draw(self):
        print(f"Drawing a {self.colour} cube with edge length {self.length}.")
        # Forming the window screen 
        tut = turtle.Screen() 
        
        # background color green 
        tut.bgcolor("green") 
        
        # window title Turtle 
        tut.title("Turtle") 
        my_pen = turtle.Turtle() 
        
        # object color 
        my_pen.color("yellow") 
        tut = turtle.Screen()            
        
        # forming front square face 
        for i in range(4): 
            my_pen.forward(100) 
            my_pen.left(90) 
        
        # bottom left side 
        my_pen.goto(50,50) 
        
        # forming back square face 
        for i in range(4): 
            my_pen.forward(100) 
            my_pen.left(90) 
        
        # bottom right side 
        my_pen.goto(150,50) 
        my_pen.goto(100,0) 
        
        # top right side 
        my_pen.goto(100,100) 
        my_pen.goto(150,150) 
        
        # top left side 
        my_pen.goto(50,150) 
        my_pen.goto(0,100)

        turtle.done()