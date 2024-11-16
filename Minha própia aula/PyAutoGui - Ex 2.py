# Exercício 2: Automatize o processo de escrever "Python é divertido!" na tela 
# do bloco de notas.

import pyautogui
import time
# # descobrir a posição
# for i in range(2): #caso precise marcar a posição de varios lugares
#     time.sleep(4)
#     posicao = pyautogui.position()
#     print(f"Posição é {posicao}")

# Pausa padrão entre comandos para dar tempo ao programa
pyautogui.PAUSE = 0.5

# abrir o bloco de notas
pyautogui.hotkey('win', 'r')
pyautogui.write('notepad.exe')
pyautogui.press('enter')

pyautogui.hotkey('alt', 'space')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write('   Python e divertido!', interval=0.25)
pyautogui.press('enter')
pyautogui.write('   PyAutoGui e melhor ainda!', interval=0.25)
