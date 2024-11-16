#11.	Produto Escalar entre Vetores: Implemente uma função 
# produto_escalar(vetor1, vetor2) que retorna o produto escalar entre dois 
# vetores (listas de números) de mesmo tamanho.

def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho")

    produto = sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))
    return produto
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_escalar(vetor1, vetor2)
print(resultado)  # Saída: 32 (1*4 + 2*5 + 3*6)
