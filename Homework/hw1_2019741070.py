from turtle import*

import turtle as t

"""t.speed('fastest')"""

def oval(rad, div, pencolor, fillcolor, pensize):
    t.pensize(pensize)
    t.color(pencolor, fillcolor)
    t.seth(-45)
    for x in range(2):
        t.begin_fill()
        t.circle(rad,90)
        t.circle(rad//div,90)
        t.end_fill()

t.penup()
t.home()
t.goto(200,200)
t.pendown()
t.pensize(5)
t.color("dimgrey")
t.begin_fill()
t.seth(180)
t.forward(400)
t.seth(270)
t.forward(400)
t.seth(0)
t.forward(400)
t.seth(90)
t.forward(400)
t.end_fill()

t.penup() 
t.home()
t.pensize(5)
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.color("white","darkgoldenrod")
t.circle(200)
t.end_fill()

t.penup()
t.goto(0,-150)
t.seth(0)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(80)
t.end_fill()

t.penup()
t.goto(0,-130)
t.pendown()
t.begin_fill()
t.color('darkgoldenrod')
t.circle(80)
t.end_fill()

t.penup()
t.home()
t.pendown()
t.dot(50,"sandybrown")

t.penup()
t.goto(50,50)
t.pendown()
t.pensize(10)

oval(50,2,"black", "blue", 5)

t.penup()
t.home()
t.goto(-150,50)
t.pendown()

oval(100,10,"black", "lightblue", 3)



t.hideturtle()



t.done()