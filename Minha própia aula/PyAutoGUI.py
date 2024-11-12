    # 1. Introdução (2 minutos) 
# PyAutoGUI: Biblioteca que permite automatizar movimentos do mouse e teclado, útil para automação de tarefas repetitivas.


    # 2. Instalação e Importação (5 minutos)
# PyAutoGUI não vem com o Python, então precisa ser instalado:
# bash
import pyautogui

    # 3. Uso Básico do pyautogui (5 minutos)
# Objetivo: Ensinar como automatizar ações de mouse e teclado.

# Mover o mouse:
pyautogui.moveTo(100, 100)  # Move o mouse para a posição x=100, y=100

# Clicar com o mouse:
pyautogui.click()  # Clica na posição atual do mouse

# Teclar (digitar texto):
pyautogui.write('Olá, mundo!')

# Captura de tela:
screenshot = pyautogui.screenshot()  # Faz uma captura de tela
screenshot.save('screenshot.png')  # Salva a captura


    # 5. Exercícios (3 minutos)
# Exercícios para os alunos:
# Use o pyautogui para mover o mouse para uma posição aleatória na tela.
# Automatize o processo de escrever "Python é divertido!" na tela com pyautogui.write().

