# Viết chương trình vẽ cây thông Noel

import turtle as t  
from turtle import *
import random as r

def draw_light():  
    if r.randint(0, 30) == 0:  
        color('red')  
        circle(r.randint(3, 6))  
    elif r.randint(0, 30) == 1:
        color('dodger blue')  
        circle(r.randint(3, 6))  
    elif r.randint(0, 30) == 2:
        color('gold')  
        circle(r.randint(3, 6))  
    else:
        color('green')  

def tree(d, s): 
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    draw_light()  
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)

def draw_snow():  
    t.ht() 
    t.pensize(2) 
    for i in range(200): 
        t.pencolor("white")  
        t.pu() 
        t.setx(r.randint(-350, 350))  
        t.sety(r.randint(-100, 350)) 
        t.pd()  
        dens = 6  
        snowsize = r.randint(1, 10) 
        for j in range(dens): 
           
            t.fd(int(snowsize))
            t.backward(int(snowsize))
           
            t.right(int(360 / dens))  

t.setup(1000, 1000)
n = 100.0

speed("fastest") 
screensize(bg='black')  
left(90)
forward(3 * n)
color("red", "yellow")  
begin_fill()
left(126)

# Vẽ ngôi sao
for i in range(5):  
    forward(n / 5)
    right(144)  
    forward(n / 5)
    left(72)  
end_fill()
right(126)

# Vẽ thân cây
color("chocolate4")  
backward(n * 4.8)

# Vẽ cây
tree(15, n)
backward(n / 2)

# Vẽ chân đế
for i in range(200):  
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 5) == 0:
        color('peru')
        circle(r.randint(3, 6))
    elif r.randint(0, 5) == 1:
        color('orange red')
        circle(r.randint(3, 6))
    elif r.randint(0, 5) == 2:  
        color('red')  
        circle(r.randint(3, 6))  
    elif r.randint(0, 5) == 3:
        color('dodger blue')  
        circle(r.randint(3, 6))  
    elif r.randint(0, 5) == 4:
        color('gold')  
        circle(r.randint(3, 6))
    elif r.randint(0, 5) == 4:
        color('pink')  
        circle(r.randint(3, 6))  
    else:
        color('green')  
        circle(r.randint(3, 6))  
    up()
    backward(a)
    right(90)
    backward(b)

t.backward(48)
t.color("red", "red") 
t.write("Merry Christmas 2023", align="center", font=("arial", 36, "bold"))
t.backward(24)
t.color("yellow", "yellow") 
t.write("Vincent", align="center", font=("arial", 16, "bold"))
t.backward(24)
t.color("yellow", "yellow") 
t.write("", align="center", font=("arial", 16, "bold"))

draw_snow()  
t.done()  