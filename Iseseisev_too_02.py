import turtle

def uks(x,y,pikkus,korgus):
    turtle.penup()
    turtle.goto(x+(pikkus/4),y)
    turtle.pendown()
    if korgus > pikkus/2:
        turtle.color("blue")
    else:
        turtle.color("red")
    for i in range(2):
        turtle.fd(pikkus/2)
        turtle.lt(90)
        turtle.fd(korgus)
        turtle.lt(90)

def katus(x,y,pikkus):
    turtle.penup()
    turtle.goto(x,y+pikkus)
    turtle.pendown()
    turtle.color("green")
    for i in range(3):
        turtle.fd(pikkus)
        turtle.left(120)

def seinad(x,y,pikkus):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("black")
    for i in range(4):
        turtle.fd(pikkus)
        turtle.lt(90)

def maja(x,y,pikkus,ukse_korgus):
    uks(x,y,pikkus,ukse_korgus)
    katus(x,y,pikkus)
    seinad(x,y,pikkus)

pikkus = 175
x = pikkus+pikkus/4
y = 0

turtle.speed(0)
turtle.width(2)

for i in range(10):
    if i < 5:
        maja(x*i,y,pikkus,pikkus/2)
    else:
        maja(x*(i-5),y-(pikkus*2+pikkus/4),pikkus,((pikkus/4)*3))

turtle.ht()
turtle.done()