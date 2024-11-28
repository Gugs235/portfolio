# # POO - Pilares
# # Abstração - refere-se a mostrar apenas os detalhes essenciais de um objeto ou classe e esconder a complexidade desnecessária
# # Encapsulamento - foca em proteger os dados internos e controlar o aceso a esses dados
# # Heranaça - erda caracteristica - capta similiaridade entre classes dispondo em hierarquia 
# # Polimorfismo - é a capacidade de um mesmo comportamento diferente em classes diferentes

# # Encapsulamento - principio do ocultamento
#     # esta ligado a permissões
#     # para vc privar o atributo ou método, basta inserir __ (dois underscores)

# class encapsulamento():
#     def __init__(self, num1, num2):
#         self.__num1 = num1
#         self.__num2 = num2
    
#     def adicionar(self):
#         return self.__num1 + self.__num2
    
# calc = encapsulamento(20,10)
# print(calc.adicionar())
# calc.__num1

#     # se eu chamar o atributo encapsulado ele da erro, mostra q não tem esse atributo

# # Herança - permite que uma classe herde dados e comportamentos de outra
#     # Vantagens
#         # Reuso
#         # Polimorfismo
#     # Definições
#         # Superclasse (classe base) / subclasse (classe derivada)
#         # Herença / extensão

# # Polimorfismo - É a capacidade de uma subclasse tem de ter métodos com o mesmo nome de sua super classe

# class Super:
#     def hello(self):
#         print("Olá, sou a superclasse!")
#     def printar(self):
#         print("Função printar")

# class Sub(Super):
#     def hello(self):
#         print("Olá, sou a subclasse!")

# class Subsub (Sub):
#     def hello(self):
#         print("Olá, sou a subsubclasse!")
# Teste = Subsub()
# Teste.hello()
# Teste.printar()
