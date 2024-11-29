class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def tipo_combustivel(self):
        return "Desconhecido"

    def capacidade_passageiros(self):
        return 0


class Carro(Veiculo):
    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 5


class Moto(Veiculo):
    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 2


class Caminhao(Veiculo):
    def tipo_combustivel(self):
        return "Diesel"

    def capacidade_passageiros(self):
        return 2
