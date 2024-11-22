# Crie um aclasse que modele um quadrado:
# atributos: tamanho do lado
# métododos:
    # mostrar_area
    # mudar_valor_lado (retorna o valor do lado e calcula area)

class Quadrado():
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mostrar_area(self):
        print(f"Sua area é: ")

    def mudar_valor_lado(self):
        lado = input("Qual é a nova cor? ")
        return lado


qdd1 = Quadrado(50)
area = lado * lado
print(f"A área é {qdd1.cor}")
qdd1.troca_cor()
qdd1.mostra_cor()
