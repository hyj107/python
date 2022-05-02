# 303p 11
import turtle, random

x1=-300
x2=-300

one = turtle.Turtle()
one.color("blue")
one.shape("arrow")

two = turtle.Turtle()
two.color("red")
two.shape("turtle")

for i in range(5):
    die = [1,2,3,4,5,6]
    distance1 = random.choice(die)
    dis1=distance1*30
    distance2 = random.choice(die)
    dis2=distance2*30
    
    one.penup()
    one.goto(x1, 0)
    x1=dis1+x1
    one.pendown()
    one.fd(dis1)
    
    two.penup()
    two.goto(x2, 100)
    x2=dis2+x2
    two.pendown()
    two.fd(dis2)

turtle.mainloop()
turtle.bye()