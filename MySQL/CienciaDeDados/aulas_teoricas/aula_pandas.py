import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df.set_index("PassengerId", inplace=True)
# df.head() # Mostra as primeiras linhas

# print(df.describe) # Descrição
# print(df.columns) # Colunas
# print(df.values) # Valores

#localizar a primeira linha
# print(df.loc[1])

# print(df.loc[10:20:2]) #localizar a linha 10 até a 20 de 2 em 2
# print(df.loc[10:20:2, "Name"]) #localizar a linha 10 até a 20 de 2 em 2 e a coluna Name

# print(df.loc[1:10, ["Name","Sex","Age"]]) #localizar a linha 1 até a 10 e as colunas Name, Sex e Age

# print(df.query('Age > 20').head())    #localizar as linhas onde a idade é maior que 20
# print(df.query('Age > 20'))           #localizar as linhas onde a idade é maior que 20
