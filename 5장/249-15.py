# -*- coding: utf-8 -*-
#249p 15번

import turtle
t= turtle.Turtle()
t.shape("turtle")

def draw_spuare(size):
    for i in range(40): #사각형 반복횟수 조정
        t.fd(size)
        t.left(90)
        size=size+5

size=0      #간격 조정
draw_spuare(size)

turtle.mainloop()
turtle.bye()
        


