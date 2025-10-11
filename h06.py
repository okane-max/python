import turtle
import math

def harjutus6_1():
    nurk = 53
    korgus = 440
    kaugus = korgus/(math.tan(math.radians(53)))
    #hypotenuus = math.sqrt(kaugus**2 + korgus**2)
    hypotenuus = math.hypot(kaugus,korgus)
    print(f"kaugus = {kaugus:0.2f} ja redeli pikkus = {hypotenuus:0.2f}")
    turtle.fd(kaugus)
    turtle.lt(90)
    turtle.fd(korgus)
    turtle.lt(90+nurk)
    turtle.fd(hypotenuus)
    turtle.done()

#harjutus6_1()
    
