

class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valor_dos_lados(self):
        self.ladoA = float(input("Novo valor A: "))
        self.ladoB = float(input("Novo valor B: "))

    def valor_lados(self):
        print(f"Lado A: {self.ladoA} | Lado B: {self.ladoB}")
    
    def calc_area(self, pisos):
        self.area = 2 * (self.ladoA + self.ladoB)
        print(f"Area igual a {self.area}, a quantidade de pisos necessarios será de {self.area / pisos}")
    
    def calc_perimetro(self, rodape):
        self.perimetro =  self.ladoA + self.ladoB
        print(f"Perimetro igual a {self.perimetro}, a quantidade para o rodapé necessario será {self.perimetro / rodape}")
    
local = Retangulo(8, 8)
piso = 2
local.calc_area(piso)
rodape = 2
local.calc_perimetro(rodape)
