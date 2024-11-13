# Escreva uma função calcula_juros_compostos(capital, taxa, tempo) que retorne o 
# montante final.

def calcula_juros_compostos(capital, taxa, tempo):
    taxa_decimal = taxa / 100
    
    # Fórmula de juros compostos: M = C * (1 + i) ** t
    montante = capital * (1 + taxa_decimal) ** tempo
    
    return montante

capital_inicial = float(input("Digite o valor do capital inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
tempo_aplicacao = int(input("Digite a quantidade de anos: "))
montante_final = calcula_juros_compostos(capital_inicial, taxa_juros, tempo_aplicacao)
print(f"Montante final: R${montante_final:.2f}")
