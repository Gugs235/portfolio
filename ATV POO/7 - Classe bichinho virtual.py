# crie uma classe que modele um tamagushi(bichinho eletronico)
# Atributos: nome, fome, saúde, idade. retornar nome, fome, saude, e idade. 
# obs: existe mais uma informação que devemos levar em consideração, o humor do nosso tamagushi, este humor é uma 
# combinação dos atributos fome e saude, ou seja, um campo calculado, então não devemos criar um atributo para 
# armazenar esta informação por que ela pode ser calculada a qualquer momento

class Tamagushi:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    # Métodos para retornar os atributos
    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    # Método para calcular o humor
    def get_humor(self):
        humor = (self.saude - self.fome) / 2
        return max(0, min(humor, 100))  # Garante que o humor esteja entre 0 e 100

    # Métodos para modificar os atributos
    def set_nome(self):
        novo_nome = input("Digite o novo nome do Tamagushi: ")
        self.nome = novo_nome

    def set_fome(self):
        nova_fome = int(input("Digite o novo valor da fome (0 a 100): "))
        self.fome = max(0, min(nova_fome, 100))  # Garante fome entre 0 e 100

    def set_saude(self):
        nova_saude = int(input("Digite o novo valor da saúde (0 a 100): "))
        self.saude = max(0, min(nova_saude, 100))  # Garante saúde entre 0 e 100

    def set_idade(self):
        nova_idade = int(input("Digite a nova idade do Tamagushi: "))
        self.idade = max(0, nova_idade)  # Idade não pode ser negativa

    # Exibir informações do Tamagushi
    def exibir_status(self):
        print(f"\n=== Status do Tamagushi ===")
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}")
        print(f"Saúde: {self.saude}")
        print(f"Idade: {self.idade}")
        print(f"Humor: {self.get_humor()}\n")


# Exemplo com inputs do usuário
nome = input("Digite o nome do seu Tamagushi: ")
fome = int(input("Digite o valor inicial da fome (0 a 100): "))
saude = int(input("Digite o valor inicial da saúde (0 a 100): "))
idade = int(input("Digite a idade inicial do Tamagushi: "))

bichinho = Tamagushi(nome, fome, saude, idade)

while True:
    print("\n=== Menu do Tamagushi ===")
    print("1. Exibir status")
    print("2. Alterar nome")
    print("3. Alterar fome")
    print("4. Alterar saúde")
    print("5. Alterar idade")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        bichinho.exibir_status()
    elif opcao == 2:
        bichinho.set_nome()
    elif opcao == 3:
        bichinho.set_fome()
    elif opcao == 4:
        bichinho.set_saude()
    elif opcao == 5:
        bichinho.set_idade()
    elif opcao == 0:
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
