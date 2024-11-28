# atividade 13
class Super():
    def __init__(self):
        self.nome = input("\nEscreva seu nome: ")
        self.idade = input("Digite sua idade: ")
        self.cpf = input("Digite seu CPF: ")
        self.email = input("Digite seu email: ")
        self.telefone = input("Digite seu telefone: ")
        self.endereco = input("Digite seu endereço ")
        self.data_de_nascimento = input("Digite sua data de nascimento: ")
        self.cidade_natal = input("Digite sua cidade natal (cidade em que você nasceu) ")
        self.nome_mae = input("Digite o nome de sua mãe: ")
        self.nome_pai = input("Digite o nome de seu pai: ")

class PF(Super):
    def __init__(self):
        super().__init__()
        self.nome = input("\nEscreva seu nome: ")
        self.idade = input("Digite sua idade: ")
        self.cpf = input("Digite seu CPF: ")
        self.telefone = input("Digite seu telefone: ")
        self.email = input("Digite seu email: ")

class PJ(Super):
    def __init__ (self):
        super().__init__()
        self.cnpf = input("\nEscreva o CNPJ da empresa: ")
        self.n_empresa = input("Escreva o nome da empresa: ")
        self.j_endereco = input("Escreva o endereço da empresa: ")
        self.contato_empresarial = input("Digite o contato da empresa: ")
        self.porte_da_empresa = input("Digite o porte da empresa: ")
