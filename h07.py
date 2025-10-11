def harjutus7_1():
    massiiv = ('1. ALIKA – “Bridges”',
    '2. Anett x Fredi – “Read Between The Lines”',
    '3. villemdrillem – “leekiv armastus”',
    '4. Clicherik & Mäx – “PAKSUD”',
    '5. nublu – “ära ärata”',
    '6. NOËP – “Move Your Feet”',
    '7. Trad.Attack! – “Bring It On”',
    '8. Bedwetters – “It Is What It Is”',
    '9. Reket – “Panama paberid”',
    '10. Grete Paia – “Võluväel”')
    
    print(20*"-"," KÕIK LOOD ",20*"-")
    for i in massiiv:
        print(i)
    valik = int(input("Valige laulu number mida soovite kuulata: "))
    valitud_laul = massiiv[valik-1]
    laul = (valitud_laul)[((valitud_laul).find(" ")+1):len(valitud_laul)]
    print("Valisite: " + laul)


def harjutus7_2():
    massiiv = ("jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3)
    print(f"Mõõdetav kuu: {massiiv[0]}")
    print(f"Viimase mõõtmise tulemus: {massiiv[-1]}")
    print(f"Kuvan ainult temperatuurid: {massiiv[1:]}")
    massiiv.pop(0)
    print(f"Kuu max temp {max(massiiv)} ja kuu min temp {min(massiiv)}")
    print(f"Kuu keskmine temp {sum(massiiv)/len(massiiv)}")
    print(f"-20 kraadi esines {massiiv.count(-20)} korda")
    massiiv.pop(5)
    massiiv.insert(5,22)
    massiiv.sort()


#Harjutused kutsu välja siin:
#harjutus7_1()
#harjutus7_2()