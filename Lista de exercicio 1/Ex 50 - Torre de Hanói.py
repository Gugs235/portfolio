# Implemente a função torre_hanoi(n, origem, destino, auxiliar) para resolver o 
# problema da Torre de Hanói.

def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    
    torre_hanoi(n - 1, origem, auxiliar, destino)
    
    print(f"Mova o disco {n} de {origem} para {destino}")
    
    torre_hanoi(n - 1, auxiliar, destino, origem)

n = int(input("Qual é o número de discos?: "))
torre_hanoi(n, "A", "C", "B")
