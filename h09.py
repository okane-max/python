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

    #Harjutus09_13
def harjutus9_13():
    ev_data = [
    ['vehicle', 'range', 'price'],
    ['Tesla Model Y Long Range', '330', '58990'],
    ['Volkswagen ID.4 Pro', '260', '39995'],
    ['Ford Mustang Mach-E', '300', '42995'],
    ['Audi e-tron GT', '238', '102700'],
    ['Nissan Leaf', '149', '27400'],
    ['BMW iX xDrive50', '324', '83995'],
    ['Polestar 2', '265', '45500'],
    ['Kia EV6 Long Range', '310', '47795'],
    ['Mercedes-Benz EQS 450+', '350', '102310'],
    ['Hyundai Kona Electric', '258', '37400']
    ]
    suurem = []

    u_kokku = 0
    h_kokku = 0
    parim_hind = 1000
    parim_auto = ""

    for i in ev_data:
        print(f"{i[0]:30} {i[1]:10} {i[2]:10}")
        if i[1].isnumeric() == True:
            km_tasu = int(i[2])/int(i[1])
            if km_tasu < parim_hind:
                parim_hind = km_tasu
                parim_auto = i[0]
            u_kokku += int(i[1])
            h_kokku += int(i[2])
            if int(i[1]) > 300:
                suurem.append(i[0])

    print("Keskmine ulatus: " + str(u_kokku/10) +"\n"+ "Keskmine hind: " + str(h_kokku/10))
    print("Läbisõidu ulatus on suurem kui 300 km")
    for i in suurem:
        print(i)
    print("Parima hinnaga auto: " + str(parim_auto))