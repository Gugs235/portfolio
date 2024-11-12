# # o tradutor é 'uma lista' mas sem os números. com ele eu consigo definir o nome do indice e fazer pesquisas a partir disso

# tradutor = {}
# tradutor ["pineapple"] = "abacaxi"
# tradutor ["apple"] = "maça"
# tradutor ["orange"] = "laranja"
# print(type(tradutor))
# print(tradutor)


# tradutor1 = {}
# tradutor1 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
# print(type(tradutor1))
# print(tradutor1)

# # aqui mostra o que tem dentro da indice
# tradutor2 = {}
# tradutor2 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
# print(tradutor2["apple"])


# # apagando uma indice apaga tambem tudo o que tem dentro
# tradutor3 = {}
# tradutor3 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
# print(tradutor3)
# del(tradutor3 ["apple"])
# print(tradutor3)
# print(tradutor3.pop('apple','Fruta não encontrada'))


# # clear() - remove todos os elementos do dicionario
# tradutor3.clear()
# print(tradutor3)


# # checa se tem ou não algo
# tradutor4 = {}
# tradutor4 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
# print("pineapple" in tradutor4)


# # checa o conteudo da indice de tem o que procuro
# tradutor4 = {}
# tradutor4 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
# print("maça" in tradutor4.values())


# # Substituit conteudo
# tradutor6 = {}
# tradutor6 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
# print(tradutor6)
# tradutor6 ["apple"] = "goiaba"
# print(tradutor6)


# # da para colocar mais conteudos em uma indice
# dados = {'Crossfox': {'km' : 35000, 'ano' : 2005} , 'DS5' : {'km' : 17000, 'ano' : 2015} , 
# 'Fusca' : {'km' : 130000, 'ano': 1979}, 'Jetta' : {'km' : 56000, 'ano' : 2011} , 'Passat' : {'km' : 62000, 'ano': 1999}}
# print (dados)


# # faz uma pesquisa, mas diferente do pop, ele não apaga
# print(dados.get('Gol', 'veiculo não encontrado'))


