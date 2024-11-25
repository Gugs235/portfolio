# Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do corretista e saldo.
# Os métodos são os seguintes: alterar_nome, depósito e saque; 
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaBancaria:
    def __init__(self, numero_conta, nome_correntista, saldo=00.00):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        print(f"O nome do correntista foi alterado para {novo_nome}.")

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

conta = ContaBancaria(12345, "João Silva", 500.00)
print(f"O número da conta é {conta.numero_conta}")
print(f"O nome do corretista é {conta.nome_correntista}")
print(f"O saldo atual da conta é {conta.saldo}\n")
conta.alterar_nome("Maria Souza")
conta.deposito(200.00)
conta.saque(100.00)
