import matplotlib.pyplot as plt

# Lista dos candidatos
candidatos = [
    "Adriane Lopes",
    "Rose Modesto",
    "Beto Pereira",
    "Camila Jara",
    "Beto Figueiró",
    "Luso De Queiroz",
    "Ubirajara Martins",
    "Jorge Batista"
]

# Lista com o número de votos no primeiro turno
votos = [
    140913,
    131525,
    115516,
    41966,
    10885,
    3108,
    1067,
    0
]

# Cria um gráfico de barras
plt.bar(candidatos, votos)
plt.grid(True)  # Adiciona a grade

# cor das barras
plt.bar(candidatos, votos, color='#FF5733')

plt.xlabel('Candidatos')

#mudando a rotação da legenda do número de votos
plt.ylabel('Número de Votos', rotation=0)

plt.title('Resultado do Primeiro Turno')
plt.xticks(rotation=45)  # Rotaciona os nomes dos candidatos para melhor visualização
plt.tight_layout()  # Ajusta a posição das etiquetas para evitar sobreposição

# mostrando o número de votos em cima das barras
for i, v in enumerate(votos):
    plt.text(i, v + 1000, str(v), ha='center', fontsize=8, color='black')


plt.show()