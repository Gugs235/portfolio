    # 1. Introdução (2 minutos) 
# Turtle: Biblioteca para criar gráficos e animações com base em comandos de movimento, útil para aprendizado visual de programação.


    # 2. Instalação e Importação (5 minutos)
# A biblioteca turtle já vem instalada no Python, então não é necessário instalar nada.
# Importação
import turtle


    # 3. Uso Básico do turtle (7 minutos)

# Criar uma tela (janela) do turtle:
turtle.setup(500, 500)

    # Mover o "tartaruga" para desenhar:
# Movimento para frente:
turtle.forward(100)  # Move 100 pixels para frente

# Virar à direita ou esquerda:
turtle.right(90)  # Vira 90 graus à direita
turtle.left(90)   # Vira 90 graus à esquerda

# Exemplo de um quadrado:
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.done()

    # Cor e estilo do traço:
# Cor do traço:
turtle.pencolor("red")  # Muda a cor para vermelho

# Cor de preenchimento:
turtle.begin_fill()
turtle.circle(50)  # Desenha um círculo
turtle.end_fill()


    # 5. Exercícios (3 minutos)
# Exercícios para os alunos:
# Desenhe um triângulo equilátero com a turtle.
# Faça a turtle desenhar um círculo de cor azul e preencher de vermelho.
