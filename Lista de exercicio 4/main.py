from sistema import cadastrar_veiculos, exibir_veiculos

if __name__ == "__main__":
    veiculos_cadastrados = cadastrar_veiculos()
    exibir_veiculos(veiculos_cadastrados)
