class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self):
        self.cor = input("Qual é a nova cor? ")

    def mostra_cor(self):
        print(f"Sua nova cor é {self.cor}")

bola1 = Bola("vermelho", 40, "pvc")
print(f"A cor é {bola1.cor}")
bola1.troca_cor()
bola1.mostra_cor()
