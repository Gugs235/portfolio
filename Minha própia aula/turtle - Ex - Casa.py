import turtle

# Goto move a caneta para uma posição especifica
# desde que a caneta esteja levanta, "PENUP()", se não, ele fara uma linha até aquela posição
# t - é uma abreviação do turtle, ao inves de escrever o nome, se escreve t


# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("sky blue")  # Fundo azul claro para simular o céu

# Configuração da tartaruga
t = turtle.Turtle()
t.speed(3)  # Velocidade média

# Desenhar as paredes da casa
t.penup()
t.goto(-50, -50)  # Posiciona para o ponto de início das paredes
t.pendown()
t.color("saddle brown")
t.begin_fill()
for _ in range(4):
    t.forward(100)  # Comprimento da parede
    t.left(90)      # Ângulo para criar o quadrado
t.end_fill()

# Desenhar o telhado
t.penup()
t.goto(-60, 50)  # Posiciona para o início do telhado
t.pendown()
t.color("firebrick")
t.begin_fill()
t.goto(0, 100)   # Ponto superior do triângulo
t.goto(60, 50)   # Canto direito do telhado
t.goto(-60, 50)  # Volta ao canto esquerdo
t.end_fill()

# Desenhar uma porta
t.penup()
t.goto(-15, -50)  # Posiciona para o início da porta
t.pendown()
t.color("dark gray")
t.begin_fill()
t.setheading(90)  # Aponta para cima
for _ in range(2):
    t.forward(40)  # Altura da porta
    t.right(90)
    t.forward(30)  # Largura da porta
    t.right(90)
t.end_fill()

# Desenhar uma janela
t.penup()
t.goto(20, 0)  # Posiciona para o início da janela
t.pendown()
t.color("light blue")
t.begin_fill()
for _ in range(4):
    t.forward(20)  # Tamanho do lado da janela
    t.right(90)
t.end_fill()

# Finalizar
t.hideturtle()
turtle.done()
