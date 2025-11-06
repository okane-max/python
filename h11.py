
    #Harjutus11_1
def pikim_sona(sonad):
    return max(sonad, key=len)
sonad = ["tere","maailm","lahe","katki","tuul","ei","jah","viisnurk"]
print(pikim_sona(sonad))

    #Harjutus11_2
def kolm_pikimat_sona(sonad):
    if len(sonad) < 3:
        return "listis ei ole piisavalt sõnu"
    #jäeb hetkel pooleni


    #Harjutus11_3
def sarnased_esitahed(sona):
    sonad = sona.split(" ")
    return sonad[0][0].lower() == sonad[1][0].lower()
print(sarnased_esitahed('Vapper vares'))
print(sarnased_esitahed('Lahe Känguru'))