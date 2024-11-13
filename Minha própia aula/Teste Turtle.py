# import turtle

# # criar uma tela
# turtle.setup(800, 800)

# # Movimento para frente:
# turtle.forward(100)  # Move 100 pixels para frente

# turtle.left(90)  # Vira 90 graus à direita

# turtle.forward(100)  # Move 100 pixels para frente

# turtle.left(90)  # Vira 90 graus à direita

# turtle.forward(200)  # Move 100 pixels para frente

# turtle.left(90)  # Vira 90 graus à direita

# turtle.forward(100)  # Move 100 pixels para frente

# turtle.left(90)  # Vira 90 graus à direita

# turtle.forward(100)  # Move 100 pixels para frente

# turtle.forward(100)  # Move 100 pixels para frente

# turtle.left(90)  # Vira 90 graus à direita

# turtle.forward(100)  # Move 100 pixels para frente

# turtle.left(45)  # Vira 90 graus à direita

# turtle.forward(130)  # Move 100 pixels para frente

# turtle.left(85)  # Vira 90 graus à direita

# turtle.forward(145)  # Move 100 pixels para frente

# turtle.done()


import turtle

# Configuração inicial
t = turtle.Turtle()
t.speed(5)  # Ajusta a velocidade da tartaruga

# Função para desenhar um quadrado
def desenha_quadrado(t, tamanho):
    for _ in range(4):
        t.forward(tamanho)
        t.right(90)

# Função para desenhar um triângulo
def desenha_triangulo(t, tamanho):
    for _ in range(3):
        t.forward(tamanho)
        t.left(120)

# Desenha a base da casa (quadrado)
desenha_quadrado(t, 100)

# Posiciona a tartaruga para desenhar o telhado
t.penup()
t.goto(0, 0)
t.pendown()

# Desenha o telhado (triângulo)
desenha_triangulo(t, 100)

# Finaliza o desenho




turtle.done()
