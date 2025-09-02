# start_game_cubes.py
import time
from body_paddle import body_paddle
from turtle import Turtle, Screen

from shapes import Create_Shapes

window = Screen()
window.setup(1200, 600)
window.bgcolor('black')
window.title('CUBES GAME')
window.tracer(0)  # نوقف التحديث التلقائي

paddlee1_right = body_paddle(300,-260)
paddlee2_left = body_paddle(-300,-260)

shpaes1_for_paddle_right = Create_Shapes(100,260,100,210)
shpaes2_for_paddle_left = Create_Shapes(-100,260,-100,210)


def the_line():
    tut=Turtle()
    tut.color('white')
    tut.hideturtle()
    tut.goto(0,300)
    tut.goto(0,-300)
the_line()
def left_for_paddle_right():# # داله عشان يلف يسار
    x_core= paddlee1_right.xcor()

    if x_core > 100:
        paddlee1_right.goto(paddlee1_right.xcor() - 60, paddlee1_right.ycor())



def right_for_paddle_right():# داله عشان يلف يسار
    x_core= paddlee1_right.xcor()


    if x_core < 510:
        paddlee1_right.goto(paddlee1_right.xcor() + 60, paddlee1_right.ycor())


def left_for_paddle_left():  # # داله عشان يلف يسار
    x_core= paddlee2_left.xcor()


    if x_core > -510:
        paddlee2_left.goto(paddlee2_left.xcor() - 60, paddlee2_left.ycor())

def right_for_paddle_left():  # داله عشان يلف يسار
    x_core= paddlee2_left.xcor()


    if x_core < -100:
        paddlee2_left.goto(paddlee2_left.xcor() + 60, paddlee2_left.ycor())

def reach_fall_foalt(x,y):
    tut=Turtle()
    tut.hideturtle()
    tut.goto(x,y)
    tut.penup()
    tut.color('red')
    tut.write(arg="YOU LOST 10 CUBES !",align='center',font=('Courier',30,'normal'))



def Lose(x,y):
    tut=Turtle()
    tut.hideturtle()
    tut.goto(x,y)
    tut.penup()
    tut.color('red')
    tut.write(arg="GAME OVER !",align='center',font=('Courier',30,'normal'))
def Win(x,y):

    tut = Turtle()
    tut.goto(x,y)
    tut.hideturtle()
    tut.penup()
    tut.color('dark green')
    tut.write(arg="GREAT YOU WIN !", align='center', font=('Courier', 30, 'normal'))
def keys():
    window.listen()
    window.onkey(left_for_paddle_right, 'Left')
    window.onkey(right_for_paddle_right, 'Right')
    window.onkey(right_for_paddle_left, 'd')
    window.onkey(left_for_paddle_left, 'a')
keys()

game_on = True
from_for_paddle_right = 80
to_for_paddle_right = 560

from_for_paddle_left = -560
to_for_paddle_left = -80






shpaes1_for_paddle_right.create_new_shape(from_for_paddle_right,to_for_paddle_right)

shpaes2_for_paddle_left.create_new_shape(from_for_paddle_left,to_for_paddle_left)


while game_on and shpaes2_for_paddle_left.score.total_score < 100 and shpaes1_for_paddle_right.score.total_score <100 and shpaes1_for_paddle_right.foalt>1 and shpaes2_for_paddle_left.foalt>1:
    window.update()
    time.sleep(0.05)
    shpaes2_for_paddle_left.move()
    shpaes1_for_paddle_right.move()



    if (
            shpaes1_for_paddle_right.distance(paddlee1_right) < 60 and
            paddlee1_right.ycor() - 20 <= shpaes1_for_paddle_right.ycor() <= paddlee1_right.ycor() + 20
        ):


        if shpaes1_for_paddle_right.shapes == 'turtle' and shpaes1_for_paddle_right.colors == 'white':
            game_on = False
            Lose(300, 0)
            Win(-300, 0)
        shpaes1_for_paddle_right.triangle(0)
        shpaes1_for_paddle_right.turtle_white(5)
        shpaes1_for_paddle_right.square_(2)
        shpaes1_for_paddle_right.circle_(1)
        print(shpaes1_for_paddle_right.score.total_score)
        shpaes1_for_paddle_right.create_new_shape(from_for_paddle_right, to_for_paddle_right)
    elif shpaes1_for_paddle_right.ycor() < -310:
        if shpaes1_for_paddle_right.shapes != 'triangle' and not (shpaes1_for_paddle_right.shapes == 'turtle' and shpaes1_for_paddle_right.colors == 'white'):
            shpaes1_for_paddle_right.foalt -= 1
            shpaes1_for_paddle_right.update_for_fultes(100, 210)
        shpaes1_for_paddle_right.create_new_shape(from_for_paddle_right, to_for_paddle_right)



    if (
            shpaes2_for_paddle_left.distance(paddlee2_left) < 60 and
            paddlee2_left.ycor() - 20 <= paddlee2_left.ycor() <= paddlee2_left.ycor() + 20
        ):


        if shpaes2_for_paddle_left.shapes == 'turtle' and shpaes2_for_paddle_left.colors == 'white':
            Lose(-300, 0)
            Win(300, 0)
            game_on = False
        shpaes2_for_paddle_left.triangle(0)
        shpaes2_for_paddle_left.turtle_white(5)
        shpaes2_for_paddle_left.square_(2)
        shpaes2_for_paddle_left.circle_(1)
        print(shpaes2_for_paddle_left.score.total_score)
        shpaes2_for_paddle_left.create_new_shape(from_for_paddle_left, to_for_paddle_left)
    elif shpaes2_for_paddle_left.ycor() < -310:
        if shpaes2_for_paddle_left.shapes != 'triangle' and not (shpaes2_for_paddle_left.shapes == 'turtle' and shpaes2_for_paddle_left.colors == 'white'):
            shpaes2_for_paddle_left.foalt -= 1
            shpaes2_for_paddle_left.update_for_fultes(-100, 210)


        shpaes2_for_paddle_left.create_new_shape(from_for_paddle_left, to_for_paddle_left)

if shpaes1_for_paddle_right.score.total_score >=100:
    Win(300, 0)
    Lose(-300, 0)


elif shpaes2_for_paddle_left.score.total_score >=100:
    Win(-300, 0)
    Lose(300, 0)


if shpaes1_for_paddle_right.foalt >=10:
    reach_fall_foalt(300, 0)
    Win(-300, 0)
elif shpaes2_for_paddle_left.foalt >=10:
    reach_fall_foalt(-300,0)
    Win(300, 0)

window.exitonclick()
