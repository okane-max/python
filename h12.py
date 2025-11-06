
    #Harjutus12_3
def arveldamine(algne_saldo,toiming,summa):
    """
    lisab või eemaldab summasid pangakontolt.

    Parameetrid:
    algne_saldo: Algse saldo väärtus.
    toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote').
    summa: Summa, mida soovitakse lisada või eemaldada.

    Tagastab:
    Konto jäägi.

    Näide:
    >>> arveldamine(1000,"deposiit",122)
    >>> arveldamine(1000,"valjavote",990)
    1122
    10
    """
    if toiming == "deposiit":
        return (algne_saldo+summa)
    elif toiming == "valjavote":
        if algne_saldo-summa < 0:
            return "Kontojääk ei ole piisav"
        else:
            return (algne_saldo-summa)

algne_saldo = 1000
print(arveldamine(algne_saldo,"deposiit",122))
print(arveldamine(algne_saldo,"valjavote",990))
