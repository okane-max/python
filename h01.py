import turtle
turtle.speed(0)

#liigu kirjutamata
def moveto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#ruut
def ruut(külg):
    for i in range(4):
        turtle.fd(külg)
        turtle.lt(90)

#võrdkülgne kolmnurk
def võrdkolmnurk(külg):
    for i in range(3):
        turtle.fd(külg)
        turtle.lt(120)
        
#nime esitäht
def nimi():
    for i in range(2):
        for i in range(30):
            turtle.fd(1.6)
            turtle.lt(1)
        for i in range(30):
            turtle.fd(1.2)
            turtle.lt(1)
        for i in range(60):
            turtle.fd(1)
            turtle.lt(1)
        for i in range(30):
            turtle.fd(1.2)
            turtle.lt(1)
        for i in range(30):
            turtle.fd(1.6)
            turtle.lt(1)
    turtle.penup()
    turtle.lt(90)
    turtle.fd(16)
    turtle.rt(90)
    turtle.pendown()
    for i in range(2):
        for i in range(30):
            turtle.fd(1.2)
            turtle.lt(1)
        for i in range(30):
            turtle.fd(0.9)
            turtle.lt(1)
        for i in range(60):
            turtle.fd(0.75)
            turtle.lt(1)
        for i in range(30):
            turtle.fd(0.9)
            turtle.lt(1)
        for i in range(30):
            turtle.fd(1.2)
            turtle.lt(1)
    

moveto(-500,300)
võrdkolmnurk(200)
moveto(-100,385)
turtle.lt(90)
nimi()
turtle.done()