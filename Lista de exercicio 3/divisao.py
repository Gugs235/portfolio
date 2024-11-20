class Divisao:
    def calcular (self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b
