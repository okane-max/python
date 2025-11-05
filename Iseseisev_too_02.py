import turtle

def uks(x,y,korgus):
    turtle.penup()
    turtle.goto(x+25,y)
    turtle.pendown()
    if korgus > 50:
        turtle.color("blue")
    else:
        turtle.color("red")
    for i in range(2):
        turtle.fd(50)
        turtle.lt(90)
        turtle.fd(korgus)
        turtle.lt(90)

def katus(x,y):
    turtle.penup()
    turtle.goto(x,y+100)
    turtle.pendown()
    turtle.color("green")
    for i in range(3):
        turtle.fd(100)
        turtle.left(120)

def seinad(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("black")
    for i in range(4):
        turtle.fd(100)
        turtle.lt(90)

def maja(x,y,ukse_korgus):
    uks(x,y,ukse_korgus)
    katus(x,y)
    seinad(x,y)


x = 125
y = 0

turtle.speed(0)
turtle.width(2)

for i in range(10):
    if i < 5:
        maja(x*i,y,50)
    else:
        maja(x*(i-5),y-225,75)

turtle.ht()
turtle.done()