# Crie um aclasse que modele um quadrado:
# atributos: tamanho do lado
# métododos:
    # mostrar_area
    # mudar_valor_lado (retorna o valor do lado e calcula area)

class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mostrar_area(self):
        area = self.tamanho_do_lado ** 2
        print(f"Sua área é: {area}")

    def mudar_valor_lado(self):
        novo_lado = float(input("Qual é o novo tamanho do lado? "))
        self.tamanho_do_lado = novo_lado

qdd1 = Quadrado(50)
qdd1.mostrar_area()
qdd1.mudar_valor_lado()
qdd1.mostrar_area()
