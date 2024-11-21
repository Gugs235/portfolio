# Programação orientada a objetos = POO

# apenas um paradigma, o código em si ou a forma de codar não muda
# TUDO É UM OBJETO!! "Super variavel"
# metodo é uma função
# todo obgjeto tem uma instancia (Uma "animação" ou ação)
# Classe -     atributo      -     metodo
# Classe - "Caracteristicas" - "Comportamento"
# o comportamnto depende dos atributos
# a ideia da classe é não ficar repetindo código
# a Classe á a parte mais facil e basica do orientada a obijetos

# como iniciar??
#  class Vendedor():
    # def _init_(self, nome, vendas):
        # self.nome = nome
        # self.vendas = vendas

#  class Nome():
    # def _init_(self, parametro):
        # self.parametro = parametro
        # self.parametro = parametro

# # Convensão o nome da função começar em letra maiuscula, e se for composta, inicio das palavras maiusculas
# _init_ = método constutor = Quando eu chamar a classe vendedor eu tenho que informar o nome e as vendas
# self = sempre que tivermos o self, significa que são caracteristicas da classe (não é um atributo da classe, ele é "ignorado") serve tambem como um retur, pq eu não posso usar aquela variavel em outro lugar, a não ser se tiver o self
# 



class Vendedor():
    def _init_(self, nome, vendas):
        self.nome = nome
        self.vendas = vendas

vendedor1 = Vendedor("Ederson", 1000)
print(vendedor1.nome)
vendedor2 = Vendedor("Maria", 2000)
print(vendedor2.nome)
