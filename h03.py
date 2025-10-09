import turtle

def harjutus3_1():
    nimi = "juhan"
    vanus = 58
    pikkus = 1.80

    print(nimi, ",", vanus," aastat vana ja pikkus on", pikkus,"m")
    
def harjutus3_2():
    toode = "arbuusi"
    kogus = 9
    hind = 2

    print("Ma tulin ostma "+str(kogus)+" "+toode+" ja iga hind on "+str(hind)+"€")
    
def harjutus3_3():
    sihtkoht = "Haapsalu"
    paevade_arv = 4
    oobimise_hind = 45
    kokku = paevade_arv*oobimise_hind
    
    print(sihtkoht+" reis kestab "+str(paevade_arv)+" päeva, ja maksab kokku "+str(kokku)+"€")

def harjutus3_6():
    kylje_pikkus = 100
    nurk = 90
    kujundi_varv = "blue"
    x = 110
    
    turtle.pencolor(kujundi_varv)
    for j in range(3):
        for i in range(4):
            turtle.fd(kylje_pikkus)
            turtle.lt(nurk)
        turtle.penup()
        turtle.goto(x,0)
        turtle.pendown()
        x = x*2
    turtle.done()

harjutus3_6()
