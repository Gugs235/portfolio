# Vamos implementar as classes Account e BusinessAccount e fazer alguns textes

# amount = valor
# balance = saldo
# deposit = deposito
# holder = perfil
# loanLimit = limite de transações
# number = numero do cartaão
# withdraw = saque

class Account():
    def __init__(self, number: int, holder:str, balance: float):
        self.number = number
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount:float):
        # implementar o saque
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Saque Realizado")
        else:
            print("Saque invalido")

    def deposit(self, amount:float):
        # implementar deposito
        if amount > 0:
            self.balance += amount
            print("Deposito Realizado")
        else:
            print("Deposito invalido")

    def __str__(self):
        return f"Número da conta: {self.number}, Perfil: {self.holder}, Saldo: {self.balance}"


class BusinessAccount(Account):
    def __init__(self, number: int, holder: str, balance: float, loanLimit:float):
        super().__init__(number, holder, balance)
        self.loanLimit = loanLimit
    def loan(self, amount: float):
        if amount > 0 and amount <= self.loanLimit:
            self.balance += amount  # Adiciona o valor emprestado ao saldo
            self.loanLimit -= amount  # Subtrai o valor do limite disponível
            print(f"Empréstimo de {amount} realizado com sucesso.")
        else:
            print("Valor inválido ou sem limite.")


    def __str__(self):
        return f"Número da conta: {self.number}, Perfil: {self.holder}, Saldo: {self.balance:.2f}, Limite: {self.loanLimit:.2f}"


acc = Account(123,"jhonathan",500)
print(f'Primeiro print: {acc}')
acc.deposit(20)
print(f'Segundo print: {acc}')
acc.withdraw(40)
print(f'Terceira print: {acc}')


b_acc = BusinessAccount(124,'Padaria',5000,3000)
print(f'\nPrimeiro print: {b_acc}')
b_acc.deposit(500)
print(f'Segundo print: {b_acc}')
b_acc.withdraw(1000)
print(f'Terceiro print: {b_acc}')
b_acc.withdraw(30000)
print(f'Quarto print: {b_acc}')
