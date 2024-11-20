# Cada classe de operação deve ter:
# Um método chamado calcular que receba dois números como parâmetros e retorne o resultado da operação.

from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

class Calculadora:
    def __init__(self):
        self.soma = Soma()
        self.subtracao = Subtracao()
        self.multiplicacao = Multiplicacao()
        self.divisao = Divisao()

    def realizar_operacao(self, operacao, a, b):
        if operacao == "soma":
            return self.soma.calcular(a, b)
        elif operacao == "subtracao":
            return self.subtracao.calcular(a, b)
        elif operacao == "multiplicacao":
            return self.multiplicacao.calcular(a, b)
        elif operacao == "divisao":
            return self.divisao.calcular(a, b)
        else:
            raise ValueError("Operação inválida.")
