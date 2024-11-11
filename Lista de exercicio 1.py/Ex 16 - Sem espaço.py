def retira_espacos(texto):
    return texto.replace(" ", "")

texto = str(input("Escreva um texto: "))
texto_sem_espacos = retira_espacos(texto)
print(texto_sem_espacos)
