# 302p 9번
import turtle
t = turtle.Turtle()
t.shape("classic")

aList=[10,20,30,40,50,60,70,80,90,100,110,120]

        
for i in aList:
    turtle.fd(i)
    turtle.fd(-1*i)
    turtle.rt(30)
 

turtle.mainloop()
turtle.bye()