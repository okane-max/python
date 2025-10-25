#Iseseisev töö 1

    #1.1. Tervitus
def ylesanne1_1():
    print("Tere, maailm!")

    #1.2. Aasta liblikas
def ylesanne1_2():
    aasta = 2020
    liblikas = "teelehe-mosaiikliblikas"
    lause_keskosa = ". aasta liblikas on "
    lause = str(aasta) + lause_keskosa + liblikas
    print(lause)

    #1.3. Pilved
def ylesanne1_3():
    korgus = float(input("Mis on pilvede aluse kõrgus? "))
    if korgus > 6.0:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")

    #1.4. Bussid
def ylesanne1_4():
    inimeste_arv = int(input("Sisestage reisijate arv: "))
    kohtade_arv = int(input("Sisestage bussi kohtade arv: "))
    busside_arv = int(inimeste_arv // kohtade_arv)
    ylejaak = inimeste_arv % kohtade_arv
    if ylejaak != 0:
        busside_arv += 1
        print("Busse vaja: " + str(busside_arv))
        print("Viimases bussis inimesi: " + str(ylejaak))
    else:
        print("Busse vaja: " + str(busside_arv))
        print("Viimases bussis inimesi: " + str(kohtade_arv))

#ylesanne1_1()
#ylesanne1_2()
#ylesanne1_3()
#ylesanne1_4()