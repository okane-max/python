#harjutus4_5



#harjutus4_4
try:
    maht = 5
    kingitused = int(input("Lisa kingituste arv: "))
    kinkekarbid = int(kingitused/maht)
    ulejaak = kingitused%maht
    print("Saad teha " + str(kinkekarbid) + " täis kinkekasti. Üle jääb " + str(ulejaak) + "kingitust.")
except:
    print("Kontrolli sisestust!")


#harjutus4_2
ale = 0.3
hind = 18.50
kogus = int(input("Sisesta raamatute kogus: "))
summa = (hind-hind*ale)*kogus
print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€.")


#harjutus4_1
a = int(input("Lisa külg 1: "))
b = int(input("Lisa külg 2: "))

p = (a+b)*2
print(f"Aia kogupikkus külgedega {a} ja {b} on {p} meetrit.")