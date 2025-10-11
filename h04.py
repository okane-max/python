import turtle

def harjutus4_1():
    a = int(input("Lisa külg 1: "))
    b = int(input("Lisa külg 2: "))

    p = (a+b)*2
    print(f"Aia kogupikkus külgedega {a} ja {b} on {p} meetrit.")


def harjutus4_2():
    ale = 0.3
    hind = 18.50
    kogus = int(input("Sisesta raamatute kogus: "))
    summa = (hind-hind*ale)*kogus
    print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€.")


def harjutus4_4():
    try:
        maht = 5
        kingitused = int(input("Lisa kingituste arv: "))
        kinkekarbid = int(kingitused/maht)
        ulejaak = kingitused%maht
        print("Saad teha " + str(kinkekarbid) + " täis kinkekasti. Üle jääb " + str(ulejaak) + "kingitust.")
    except:
        print("Kontrolli sisestust!")


def harjutus4_5():
    try:
        raadius = float(input("Sisestage ringi raadius: "))
        pindala = (raadius**2)*3.14
        umbermoot = 2*raadius*3.14
        print(f"Ringi pindala on {pindala:0.2f} ja ümbermõõt on {umbermoot:0.2f}")
        turtle.circle(raadius)
        turtle.done()
    except:
        print("Kontrolli sisestust!")

#Harjutused kutsu välja siin:
#harjutus4_1
#harjutus4_2
#harjutus4_4
#harjutus4_5