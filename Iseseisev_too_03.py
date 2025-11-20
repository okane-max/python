import turtle
import random

def viisnurk(pikkus):
    for i in range(5):
        turtle.fd(pikkus)
        turtle.lt(360/5)

def ring(pikkus,x,y,x_algus,y_algus):
    turtle.penup()
    turtle.goto((x+pikkus/2)+x_algus,y+y_algus)
    turtle.pendown()
    turtle.circle(pikkus/2)

def ruut(pikkus):
    for i in range(4):
        turtle.fd(pikkus)
        turtle.lt(90)
        
def suvaline(pikkus,x,y,x_algus,y_algus):
    valik = random.randint(0,2)
    if valik == 0:
        viisnurk(pikkus)
    elif valik == 1:
        ring(pikkus,x,y,x_algus,y_algus)
    else:
        ruut(pikkus)

pikkus = 50
y_algus = -300
x_algus = -300
x = 0
y = 0
kordus = 0
turtle.speed(5)
turtle.penup()
turtle.goto(x+x_algus,+y_algus)
turtle.pendown()
    
while True:
    kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ")
    kogus = int(input("Mitu kujundit soovid joonistada? "))
    for i in range(kogus):
        if kujund == "viisnurk":
            viisnurk(pikkus)
        elif kujund == "ring":
            ring(pikkus,2*x,y,x_algus,y_algus)
        elif kujund == "ruut":
            ruut(pikkus)
        else:
            suvaline(pikkus,2*x,y,x_algus,y_algus)
        kordus += 1
        if kordus > 6:
            y += pikkus*2
            x = 0
            kordus = 0
        else:
            x = pikkus*kordus
        turtle.penup()
        turtle.goto(2*x+x_algus,y+y_algus)
        turtle.pendown()
    jatkata = input("Soovid jätkata? ")
    if jatkata == "":
        print("Imetlege oma kunstiteost!")
        break
    
turtle.done()