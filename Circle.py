import turtle
import random
turtle.shape("turtle") #preference
turtle.speed(0)


#circle
def circle():
    turtle.circle(50)
circle()


#turtle olympics
def olympics():
    turtle.pencolor("green")
    turtle.circle(50)
     
    turtle.pu()
    turtle.setposition(-120, 0)
    turtle.pd()
    turtle.pencolor("yellow")
    turtle.circle(50)
     
    turtle.pu()
    turtle.setposition(60,60)
    turtle.pd()
    turtle.pencolor("red")
    turtle.circle(50)
     
    turtle.pu()
    turtle.setposition(-60, 60)
    turtle.pd()
    turtle.pencolor("black")
    turtle.circle(50)
     
    turtle.pu()
    turtle.setposition(-180, 60)
    turtle.pd()
    turtle.pencolor("blue")
    turtle.circle(50)
olympics()


#arc
turtle.pu()
turtle.goto(200, 50)
turtle.pd()
def arc():
    turtle.circle(100, 150)
arc()


turtle.pu()
turtle.goto(100, 50)
turtle.pd()
turtle.pencolor("pink")


#messycircle
def messycircle():
    for i in range(127):
        turtle.circle(5*i)
        turtle.circle(-5*i)
        turtle.left(i)
        b = i
        if b > 255:
            b = 255
messycircle()


turtle.pu()
turtle.goto(-50, 100)
turtle.pd()
turtle.pencolor("black")


#tilted circles:
def tiltcircle():
    for i in range(18):
        turtle.left(20)
        turtle.circle(50)
tiltcircle()


#random
def randomcircle():
    colours = ["blue", "black", "pink", "red", "yellow", "orange", "green"]
    while True:
        turtle.pu()
        turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
        turtle.pd()
        turtle.pencolor(colours[random.randint(0,6)])
        turtle.circle(random.randint(20, 100))
        turtle.pu()
randomcircle()
