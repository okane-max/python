import random
import turtle

def harjutus5_1():
    try:
        vanus = int(input("Sisestage oma vanus: "))
        if vanus >= 18:
            print("Võite üritusele siseneda.")
        else:
            print("Te ei ole üritusele sisenemiseks piisavalt vana.")
    except:
        print("Kontrollige sisestust!")


def harjutus5_2():
    try:
        temp = int(input("Sisestage temperatuur: "))
        if temp < 0:
            print("Soovitan teil kanda talveriideid.")
        elif temp < 15:
            print("Soovitan teil kanda kevad-sügis rõivaid.")
        else:
            print("Soovitan teil kanda suveriideid.")
    except:
        print("Kontrollige sisestust!")


def harjutus5_3():
    try:
        arv1 = random.randint(1,10)
        arv2 = random.randint(1,10)
        vastus = int(input(f"Mis on {arv1} korda {arv2}? "))
        if vastus == (arv1*arv2):
            print("Õige vastus!")
        else:
            print("Vale vastus!")
    except:
        print("Kontrollige sisestust!")

def harjutus5_4():
    try:
        munt = random.randint(0,1)
        arva = input("Arvake kumb külg maandub mündiviskamisel ülespoole? ")
        if arva.lower() == "kull" or "kiri":
            if arva.lower() == "kull" and munt == 0:
                turtle.pencolor("green")
                turtle.circle(100)
            else:
                turtle.pencolor("red")
                turtle.circle(100)
            turtle.done()
        else:
            print("Kontrollige sisestust!")
            pass
    except:
        print("Kontrollige sisestust!")


#Harjutused kutsu välja siin:
#harjutus5_1()
#harjutus5_2()
#harjutus5_3()
#harjutus5_4()