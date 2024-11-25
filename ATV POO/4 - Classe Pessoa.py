# crie uma classe que modele uma pessoa
# atributos: nome, peso, idade e altura
# métodos: envelhecer, engordar, emagrecer, crescer
# obs: Por padrão a cada ano que nossa pessoa envelhece, sendo a idade menor que 21, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def envelhecer(self):
        self.idade = int(input("Quantos anos de idade você tem agora: "))

    def engordar(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self):
        if self.idade < 21:
            self.altura = self.altura + 0.5

pessoa1 = Pessoa("Jhonathan", 5, 65, 1.75)
print(f"{pessoa1.nome} tem {pessoa1.idade} anos de idade e tem {pessoa1.altura} de altura")
pessoa1.envelhecer()
pessoa1.crescer()
print(f"Agora {pessoa1.nome} tem {pessoa1.idade} anos de idade e tem {pessoa1.altura} de altura")
