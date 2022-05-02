# p303 10ë²ˆ

import random, turtle
clist=["yellow","red","purple","blue"] #색 리스트
t=turtle.Turtle()

#예스
def draw():
   
    t.begin_fill()
    t.pencolor("black")    
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    
    t.end_fill()
    

while 1:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    
    t.shape("turtle")
    
    t.penup()
    t.goto(x, y)
    t.pendown()

    c=random.choice(clist)
    t.color(c)
    
    draw()    
    

turtle.mainloop()
turtle.bye()