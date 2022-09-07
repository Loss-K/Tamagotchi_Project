#https://www.youtube.com/watch?v=ZA4SnBWoA5Q
#Learning Turtle - potentionally to build random Tamagotchi characters later.
from turtle import Turtle

t = Turtle()

t.up()
t.screen.tracer(0)
t.goto(-200,200)
t.down()

side = 25

def bloop(s_color = "black"):
    t.color(s_color)
    t.begin_fill()
    for num in range(4):

        t.fd(side)
        t.rt(90)
    t.end_fill()
    t.fd(side)


bloop()
t.getscreen().update()
