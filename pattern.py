from turtle import *
import random
speed(0)
bgcolor("black")
x = 1
while x < 500:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colormode(255)
    pencolor(r, g, b)
    fd(50 + x)
    rt(90.911)
    x = x + 1
