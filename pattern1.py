from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
colors=["red","yellow","purple"]
t.speed(10)
t.pensize(1.2)
for x in range(100):
    t.circle(x)
    t.color(colors[x%3])
    t.left(60)
 
t.screen.exitonclick()
t.screen.mainloop()
