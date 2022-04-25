import turtle as t
import time as ti
def rectangle(hor,ver,col):# chuong trinh ve hcn
    t.pendown() 
    t.pensize(1) 
    t.color(col)
    t.begin_fill()
    for i in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()
    
def triangle(x,col1):# chuong trinh ve hinh tam giac
    t.pendown() 
    t.pensize(1) 
    t.color(col1)
    t.begin_fill()
    for i in range(3):
        t.forward(x)
        t.right(120)
    t.end_fill()
    t.penup()
    
def octagon(x1,y1,col2): # chuong trinh ve mai hbh
    t.pendown() 
    t.pensize(1) 
    t.color(col2)
    t.begin_fill()
    for i in range(1):
        t.left(30)
        t.forward(x1)
        t.left(90)
        t.forward(y1)
        t.left(90)
        t.forward(x1)
        t.left(90) 
        t.forward(y1)
    t.end_fill()
    t.penup()
    
def octagon1(x2,y2,clo3): # chuong trinh ve tuong hbh
    t.pendown() 
    t.pensize(1) 
    t.color(clo3)
    t.begin_fill()
    for i in range(1):
        t.left(30)
        t.forward(x2)
        t.left(60)
        t.forward(y2)
        t.left(120)
        t.forward(x2)
        t.left(60) 
        t.forward(y2)
    t.end_fill()
    t.penup()
# bat dau ve
t.penup()
t.speed('fast')
t.bgcolor('Dodger blue')
# mat trc
t.goto(0,0)
rectangle(60,-100,'blue')
# cua
t.goto(20,0)
rectangle(20,-50,'green')
# mai truoc
t.goto (60,100)
triangle(-60,'pink')
# mai hong
t.goto (60,100)
octagon(100,60,'orange')
# mat hong
t.goto (60,0)
t.right(-60)
octagon1(110,100,'yellow')
# cua so
t.goto(100,60)
t.right(-90)
octagon1(20,20,'red')
# cay
t.goto(300,50)
t.right(90)
rectangle(15,-50,'red')
t.goto(320,50)
triangle(60,'green')
t.goto(320,105)
triangle(60,'green')
t.goto(320,160)
triangle(60,'green')
# mat troi
t.goto(200,300)
t.fillcolor('yellow')
t.begin_fill()
t.circle(20)
t.end_fill()