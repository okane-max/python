    #Harjutus08_1
def harjutus8_1():
    telefonid={
    'Mari': '5957503',
    'Toomas': '5719979',
    'Kertu': '5201750',
    'Siim': '5580027',
    'Piret': '5960799',
    'Jaan': '5160415',
    'Lea': '5760164',
    'Mart': '5337951',
    'Anni': '5004818',
    'Tõnu': '5721873',
    'Kai': '5811884',
    'Rasmus': '5859489',
    'Eva': '5039393',
    'Oskar': '5635812',
    'Liina': '5696114',
    'Peeter': '5560756',
    'Sandra': '5257415',
    'Heiki': '5207248',
    'Kristi': '5703338',
    'Urmas': '5400549'
    }

    print("Rasmuse telefoni number: " + telefonid['Rasmus'])
    telefonid['Oliver'] = '5058505'
    del telefonid['Kristi']
    telefonid['Eva'] = '5555555'
    print(telefonid.values())
    otsitu = input("Kirjutage isiku nimi kelle telefoni numbrit otsite: ")
    if otsitu in telefonid.keys():
        print(str(otsitu) + " telefoni number on " + telefonid[otsitu])
    else:
        print("ei leidnud sellist isikut")


    #Harjutus08_2
def harjutus8_2():
    tooted = {
    'piim': {'kogus': 20, 'hind': 1.19},
    'küpsised': {'kogus': 20, 'hind': 4.99},
    'või': {'kogus': 20, 'hind': 2.29},
    'juust': {'kogus': 15, 'hind': 1.9},
    'leib': {'kogus': 15, 'hind': 2.59},
    'jogurt': {'kogus': 18, 'hind': 3.65},
    'õunad': {'kogus': 35, 'hind': 3.15},
    'apelsinid': {'kogus': 40, 'hind': 0.99},
    'banaanid': {'kogus': 23, 'hind': 1.29}
    }
    print(tooted['piim']['kogus'])

    toode = input("Sisestage toode mida soovite osta: ")
    kogus = int(input("Sisestage kogus mida te soovite osta: "))
    if toode in tooted.keys():
        if tooted[toode]['kogus'] >= kogus:
            print("Teie ost läheb maksma " + str(kogus*tooted[toode]['hind']) + " eurot")
            tooted[toode]['kogus'] -= kogus
            print(tooted)
        else:
            print("Toodet ei ole piisavalt")
    else:
        print("Toodet ei leitud")


