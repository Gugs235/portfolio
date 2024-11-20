# Implemente uma função valida_senha(senha) que verifique se uma senha atende a
# requisitos (tamanho, caracteres especiais, etc.).

# Requisitos da senha:
# A senha deve ter pelo menos 8 caracteres.
# A senha deve conter pelo menos uma letra maiúscula.
# A senha deve conter pelo menos uma letra minúscula.
# A senha deve conter pelo menos um número.
# A senha deve conter pelo menos um caractere especial (por exemplo, @, #, $, etc.).

def valida_senha(senha):
    # Verificar o tamanho mínimo
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    # Verificar se contém pelo menos uma letra maiúscula
    if not any(c.isupper() for c in senha):
        return "A senha deve conter pelo menos uma letra maiúscula."

    # Verificar se contém pelo menos uma letra minúscula
    if not any(c.islower() for c in senha):
        return "A senha deve conter pelo menos uma letra minúscula."

    # Verificar se contém pelo menos um número
    if not any(c.isdigit() for c in senha):
        return "A senha deve conter pelo menos um número."

    # Verificar se contém pelo menos um caractere especial
    caracteres_especiais = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
    if not any(c in caracteres_especiais for c in senha):
        return "A senha deve conter pelo menos um caractere especial."

    return "Senha válida."

senha_teste = input("Digite uma senha para validar: ")
print(valida_senha(senha_teste))
