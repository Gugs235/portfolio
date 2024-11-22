class ControleRemoto:
    def __init__(self, nome, cor, altura, profundidade, largura):
        self.nome = nome
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def mudar_volume(self):
        botao = input("Digite '+' para aumentar o volume ou '-' para diminuir o volume: ").strip()
        if botao == '+':
            print('Aumentando o volume...')
        elif botao == '-':
            print('Diminuindo o volume...')
        else:
            print("Entrada inválida. Tente novamente.")

# Captura de dados do controle
nome = input("Qual o nome do controle? ")
cor = input("Qual a cor do controle? ")
altura = input("Qual a altura do controle? ")
profundidade = input("Qual a profundidade do controle? ")
largura = input("Qual a largura do controle? ")

# Criação do objeto ControleRemoto
controle = ControleRemoto(nome, cor, altura, profundidade, largura)

# Exibe informações do controle
print(f"\nControle criado: Nome: {controle.nome}, Cor: {controle.cor}, Altura: {controle.altura}, Profundidade: {controle.profundidade}, Largura: {controle.largura}")

# Chamando o método para mudar o volume
controle.mudar_volume()



# while True:

#     print(ControleRemoto())
#     print(ControleRemoto.mudar_volume())

