# 199p 7번

import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

for i in range(360):
    sine = math.sin(math.pi*i/180.0)
    print(sine)
    t.goto(i,sine*100)

turtle.mainloop()
turtle.bye()
