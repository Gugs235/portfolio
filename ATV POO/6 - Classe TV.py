# Faça um programa que simule um televisor criando-o como um objeto. 
# O usuario deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas


class Televisor:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume
        self.max_canal = 100  # Número máximo de canais
        self.min_canal = 1    # Número mínimo de canais
        self.max_volume = 10  # Volume máximo
        self.min_volume = 0   # Volume mínimo

    def mudar_canal(self, novo_canal):
        if self.min_canal <= novo_canal <= self.max_canal:
            self.canal = novo_canal
            print(f"Canal alterado para: {self.canal}")
        else:
            print(f"Erro: Canal inválido. Escolha entre {self.min_canal} e {self.max_canal}.")

    def aumentar_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Volume aumentado para: {self.volume}")
        else:
            print(f"Volume já está no máximo: {self.max_volume}.")

    def diminuir_volume(self):
        if self.volume > self.min_volume:
            self.volume -= 1
            print(f"Volume diminuído para: {self.volume}")
        else:
            print(f"Volume já está no mínimo: {self.min_volume}.")

    def status(self):
        print(f"Canal atual: {self.canal}, Volume atual: {self.volume}")

tv = Televisor()

while True:
    print("\n1. Mudar canal")
    print("2. Aumentar volume")
    print("3. Diminuir volume")
    print("4. Exibir status da TV")
    print("0. Desligar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        novo_canal = int(input("Digite o número do canal: "))
        tv.mudar_canal(novo_canal)
    elif opcao == 2:
        tv.aumentar_volume()
    elif opcao == 3:
        tv.diminuir_volume()
    elif opcao == 4:
        tv.status()
    elif opcao == 0:
        print("Desligando TV...")
        break
    else:
        print("Opção inválida. Tente novamente.")
