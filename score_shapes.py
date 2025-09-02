# score_shapes.py
from  turtle import Turtle


class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.total_score = 0
        self.color('white')
        self.penup()
        self.goto(x, y)

        self.write(f'Score: {self.total_score}', align='center', font=('Arial',15,'normal'))

    def new_score(self):

        self.clear()
        self.write(f'Score: {self.total_score}', align='center', font=('Arial', 15, 'normal'))