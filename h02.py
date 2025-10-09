import turtle
turtle.speed(0)

ekraan = turtle.Screen()
ekraan.title("Olümpiarõngad Oliver Kane")
ekraan.setup(500,400)

#olümpiarõngad
turtle.pensize(6)
turtle.penup()
turtle.bk(110)
turtle.pendown()

turtle.pencolor("blue")
turtle.circle(50,360)

turtle.penup()
turtle.fd(110)
turtle.pendown()

turtle.pencolor("black")
turtle.circle(50,360)

turtle.penup()
turtle.fd(110)
turtle.pendown()

turtle.pencolor("red")
turtle.circle(50,360)

turtle.penup()
turtle.bk(55)
turtle.rt(90)
turtle.fd(55)
turtle.lt(90)
turtle.pendown()

turtle.pencolor("green")
turtle.circle(50,360)

turtle.penup()
turtle.bk(110)
turtle.pendown()

turtle.pencolor("yellow")
turtle.circle(50,360)

turtle.ht()
turtle.done()