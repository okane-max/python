import random

    #Harjutus09_1
def harjutus9_1():
    for i in range(20):
        print(i+1)

    #Harjutus09_2
def harjutus9_2():
    for i in range(20):
        print(random.randint(1,99))

    #Harjutus09_3
def harjutus9_3():
    loend = []
    for i in range(20):
        loend.append(random.randint(1,99))
    print(sum(loend))

    #Harjutus09_4
def harjutus9_4():
    for i in range(1,43):
        if i%3 == 0 and i%5 == 0:
            print(str(i) + " TIKTAK")
        elif i%3 == 0:
            print(str(i) + " TIK")
        elif i%5 == 0:
            print(str(i) + " TAK")
        else:
            print(i)

    #Harjutus09_5
def harjutus9_5():
    arvud = ""
    for i in range(200,321):
        if i%7 == 0 and i%5 != 0:
            arvud += (str(i) + ",")
    print(arvud)