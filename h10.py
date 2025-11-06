import random

    #Harjutus10_1
def harjutus10_1():
    arvud = []
    while True:
        arv = input("Sisestage arv: ")
        if arv == "":
            print(f"{sum(arvud) / len(arvud)}")
            break
        arvud.append(int(arv))

    #Harjutus10_2
def harjutus10_2():
    tulemused = []
    while True:
        juhuslik_arv = random.randint(1,10)
        katse = 1
        mang = 1
        while True:
            arvamus = input("Arvake ära number vahemikus 1-10: ")
            if int(arvamus) == juhuslik_arv:
                tulemused.append(katse)
                print("Arvasite õigesti! See võttis teil " + str(katse) + " katset.")
                break
            else:
                katse += 1
                print("Arvasite valesti!")
        kordus = input("Kas soovite mängida uuesti?(jah/ei) ")
        if kordus != "jah":
            print("Tänan mängus osalemise eest!")
            for i in tulemused:
                print(str(mang)+". mäng võttis teil "+ str(i) +" katset")
                mang += 1
            break
