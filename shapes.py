import random
from score_shapes import Score
import time
from  turtle import Turtle,Screen
from  score_shapes import Score



class Create_Shapes(Turtle):


    def __init__(self,x_for_score,y_for_score,x_fult_func,y_fult_func):
        super().__init__()
        self.penup()
        self.defulte_time= 0.05# # رفع القلم
        self.score = Score(x_for_score,y_for_score)
        self.y= 10 
        self.foalt = 10
        self.tut =Turtle()
        self.how_many_fultes_he_have(x_fult_func,y_fult_func)



    def create_new_shape(self,fromm,to):


        self.goto_list = random.randrange(fromm,to,50) # X رقم عشوائي لنقطة الذهاب الى

        self.goto(self.goto_list, 300) # الذهاب الى

        # self.shapes=random.choice(['turtle']) #   شكل عشوائي
        self.shapes=random.choice(['circle','square','turtle','triangle']) #   شكل عشوائي




        self.colors= random.choice(['red','white','purple','orange','blue','yellow','green']) # اختيار لون عشوائي
        self.colors= random.choice(['white','red']) # اختيار لون عشوائي




        self.sizes = random.choice([1,2])  #رقم عشوائي للحجم




        self.shape(self.shapes)  # الشكل




        self.color(self.colors)  # اللون

        self.shapesize(self.sizes)  # الحجم

    def triangle(self,position):
        if self.shapes =='triangle':

            self.y= 10
            self.score.total_score = position
            self.score.new_score()


    def turtle_white(self,position):

        if  self.shapes == 'turtle' and self.shapes!= 'white':
            self.high_speedd()
            self.score.total_score += position
            self.score.new_score()
    def circle_(slef,position):
        if slef.shapes == 'circle':
            slef.score.total_score +=position
            slef.score.new_score()
            slef.high_speedd()
    def square_(slef,position):
        if slef.shapes == 'square':
            slef.score.total_score +=position
            slef.score.new_score()
            slef.high_speedd()





    def move(self): #تحريك الشكل

        self.goto(self.xcor(),self.ycor()-self.y)

    def high_speedd(self):
        self.y += 0.6

    def how_many_fultes_he_have(self,x,y):

        self.tut.hideturtle()
        self.tut.goto(x,y)
        self.tut.penup()
        self.tut.color('white')

        self.tut.write(arg=f"You have {self.foalt} tries",align='center',font=('bold',11,'normal'))










    def update_for_fultes(self,x,y):

        self.tut.clear()
        self.tut.hideturtle()
        self.tut.penup()
        self.tut.color('white')
        self.tut.goto(x,y)
        self.tut.write(arg=f"You have {self.foalt} tries",align='center',font=('bold',11,'normal'))