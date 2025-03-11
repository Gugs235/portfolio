import matplotlib.pyplot as plt

valores = [151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 
           510, 540, 545, 622, 678, 724, 788, 880, 937, 954, 
           998, 1039, 1045, 1100, 1212, 1302, 1320, 1412, 1518]

anos = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
        2010, 2011, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 
        2019, 2020, 2020, 2021, 2022, 2023, 2023, 2024, 2025]

plt.plot(range(len(anos)), valores, 'ro-')  # 'ro-' para marcar os pontos em vermelho

plt.title('Salário Mínimo')  
plt.ylabel('Valor (R$)')  
plt.xlabel('Ano')  
plt.xticks(range(len(anos)), anos, rotation=45)  # Rotaciona os anos para melhor visualização

plt.legend(['Salário Mínimo'], loc='upper left')
plt.grid(True)  

# Adicionando os valores acima dos pontos
for i, valor in enumerate(valores):
    plt.text(i, valor + 30, str(valor), ha='center', fontsize=8, color='black')

plt.show()
