# atividade 13
from Polimorfismo_Pessoa import PF,PJ

while True:
    print("\n------PAGINA INICIAL-----")
    print("1 - Pessoa Física")
    print("2 - Pessoa Jurídica")
    print("0 - Desligar")
    opc = int(input("Digite o código desejado: "))

    if opc == 1:
        pessoa = PF()
    elif opc == 2:
        pessoa = PJ()
    elif opc == 0:
        print("Desligando...")
        break
    else:
        print("Código invalido")

