# Crie uma função media_notas(dicionario) que recebe um dicionário de alunos e notas 
# e retorna a média das notas.

def media_notas(dicionario):
    total_notas = 0
    total_alunos = 0

    for aluno, nota in dicionario.items():
        total_notas += nota
        total_alunos += 1

    if total_alunos == 0:
        return 0
    
    media = total_notas / total_alunos
    return media

alunos = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5,
    "Ana": 9.5
}

media = media_notas(alunos)
print(f"A média das notas é: {media:.2f}")
