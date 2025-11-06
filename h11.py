import turtle
import random
"""
    #Harjutus11_1
def pikim_sona(sonad):
    return max(sonad, key=len)
sonad = ["tere","maailm","lahe","katki","tuul","ei","jah","viisnurk"]
print(pikim_sona(sonad))

    #Harjutus11_2
def kolm_pikimat_sona(sonad):
    if len(sonad) < 3:
        return "listis ei ole piisavalt sõnu"
    #jäeb hetkel pooleni


    #Harjutus11_3
def sarnased_esitahed(sona):
    sonad = sona.split(" ")
    return sonad[0][0].lower() == sonad[1][0].lower()
print(sarnased_esitahed('Vapper vares'))
print(sarnased_esitahed('Lahe Känguru'))
"""
    #Harjutus11_4
def harjutus11_4():
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
        if kujund == "":
            print("Väljute programmist.")
            break
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
    
    turtle.done()

harjutus11_4()



    
    
    
