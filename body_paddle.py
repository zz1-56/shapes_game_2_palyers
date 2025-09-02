from  turtle import Turtle
class body_paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(6, 1)
        self.setheading(270)
        self.goto(x, y)
