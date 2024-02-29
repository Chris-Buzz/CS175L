#Christopher Buzaid
#CS 175L
#STOP
import math
import turtle
screen = turtle.Screen()

#Constants
window_height = 400
window_width = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_X = -5
text_Y = -10

turtle.setup(window_width, window_height)

s = length
x = s / math.sqrt(2)
diameter = s + (2 * x)


t = turtle.Turtle()
screen.bgcolor('white')
t.color('red')
t.begin_fill()
t.penup()
t.setpos(-40, 100)
t.pendown()


for i in range(num_sides):
        t.width(10)
        t.forward(length)
        t.right(angle)

        t.begin_fill()
t.penup()
t.setpos(-30, 75)
t.pendown()

for i in range(num_sides):
        t.forward(80)
        t.right(angle)
t.end_fill()

t.end_fill()
t.penup()
t.setpos(10,-50)
t.end_fill()
t.color('white')
t.end_fill()
t.pendown()
t.write('STOP',  align='center', font=('Arial', 40, 'bold'))
t.hideturtle()


