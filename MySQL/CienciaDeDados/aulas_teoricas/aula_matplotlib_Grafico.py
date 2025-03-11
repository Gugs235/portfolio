import matplotlib.pyplot as plt

# a = (1,2,3,4,5) # Valores de x
# b = (1,2,3,4,5) # Valores de y

# plt.plot(a,b) # Plotting a vs b
# plt.ylabel(u'eixo y') # u' para string unicode
# plt.xlabel(u'eixo x') # nome do eixo x
# plt.title('Meu gráfico') # título do gráfico
# plt.show() # Mostra o gráfico
# plt.legend(['x^2', 'x^3']) # Adiciona a legenda
# plt.subplot(2,1,1) # 2 linhas, 1 coluna, 1º gráfico
# plt.scatter((1,2,3,4,5),(1,4,9,16,25), color='r') # Gráfico de dispersão


plt.subplot(3,3,1) # 3 linhas, 3 colunas, 1º gráfico
a = (1,2,3,4,5) # Valores de x
b = (1,2,3,4,5) # Valores de y
plt.plot(a,b) # Plotting a vs b

plt.title('Primeiro Gráfico') # título do gráfico
plt.xlabel('eixo x') # nome do eixo x
plt.ylabel(u'eixo y') # nome do eixo y
plt.grid(True)  # Adiciona a grade
plt.axis((0,10,0,30)) # limites do gráfico


plt.subplot(3,3,2) # 3 linhas, 3 colunas, 2º gráfico
plt.plot((0.5,2,3,4,5),(3,6,11,18,27), 'cD-') # 'cD' é o estilo do gráfico

plt.title('Segundo Gráfico') # título do gráfico
plt.xlabel('eixo x') # nome do eixo x
plt.ylabel(u'eixo y') # nome do eixo y
plt.grid(True)  # Adiciona a grade
plt.axis((0,10,0,30)) # limites do gráfico


plt.subplot(3,3,3) # 3 linhas, 3 colunas, 3º gráfico
plt.scatter((1,2,3,4,5),(1,4,9,16,25), color='r') # Gráfico de dispersão

plt.title('Terceiro Gráfico - Dispersão') # título do gráfico
plt.xlabel('eixo x') # nome do eixo x
plt.ylabel(u'eixo y') # nome do eixo y
plt.grid(True)  # Adiciona a grade
plt.axis((0,10,0,30)) # limites do gráfico

plt.subplot(3,3,4) # 3 linhas, 3 colunas, 4º gráfico
# grafico de barras com cor em exdecimal
plt.bar((1,2,3,4,5),(1,4,9,16,25), color='#FF5733') # Gráfico de barras
plt.title('Quarto Gráfico - Barras') # título do gráfico
plt.xlabel('eixo x') # nome do eixo x
plt.ylabel(u'eixo y') # nome do eixo y
plt.grid(True)  # Adiciona a grade
plt.axis((0,10,0,30)) # limites do gráfico

plt.subplot(3,3,5) # 3 linhas, 3 colunas, 5º gráfico
plt.hist((1,2,3,4,5), bins=5, color='g') # Histograma
plt.title('Quinto Gráfico - Histograma') # título do gráfico
plt.xlabel('eixo x') # nome do eixo x
plt.ylabel(u'eixo y') # nome do eixo y
plt.grid(True)  # Adiciona a grade
plt.axis((0,10,0,30)) # limites do gráfico

plt.subplot(3,3,6) # 3 linhas, 3 colunas, 6º gráfico
a = (10, 20, 30, 45, 55, 96)
# explode, define o quanto o gráfico será "explodido", ou seja, quanto o gráfico será deslocado do centro da pizza 
explode = (0.1, 0, 0, 0, 0, 0)  # Explode apenas o primeiro elemento
labels = ["HB20", "Gol", "Onix", "Palio", "Fiesta", "Uno"]  # Agora com 6 elementos
#autopct='%.2f%%' - mostra a legenda com a porcentagem no gráfico
plt.pie(a, explode=explode, labels=labels, autopct='%.2f%%', shadow=True)
plt.title('Sexto Gráfico - Pizza')
plt.grid(True)  # Adiciona a grade





plt.show() # Mostra o gráfico
