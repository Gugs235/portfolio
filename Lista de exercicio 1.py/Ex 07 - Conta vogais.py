def conta_vogais(texto):
    (texto.lower())
    print(f"Nessa palavra tem {texto.count("a")} letra a")
    print(f"Nessa palavra tem {texto.count("e")} letra e")
    print(f"Nessa palavra tem {texto.count("i")} letra i")
    print(f"Nessa palavra tem {texto.count("o")} letra o")
    print(f"Nessa palavra tem {texto.count("u")} letra u")
    return(texto)
texto = str(input("Escreva uma palavra: "))
conta_vogais(texto)
