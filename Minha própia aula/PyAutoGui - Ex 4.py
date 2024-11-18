# Exercício 4: Aumente o volume no maximo, abra o Google Chrome na tela inicial, 
# entre no YouTube e abra a música: "You Are Good - Israel & New Breed"

import pyautogui
import time
# # descobrir a posição
# for i in range(2): #caso precise marcar a posição de varios lugares
#     time.sleep(4)
#     posicao = pyautogui.position()
#     print(f"Posição é {posicao}")

# Pausa padrão entre comandos para dar tempo ao programa
pyautogui.PAUSE = 2

# Copiando o link
#           https://youtu.be/5KiQDoWo5t4?si=pB5SpqYDdZ2O78zV
pyautogui.moveTo(513, 446)
pyautogui.click()
pyautogui.mouseDown()
pyautogui.moveTo(1045, 446)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'c')


# aumentar o volume
pyautogui.moveTo(1783, 1053)
pyautogui.click()
pyautogui.moveTo(1852, 1010)
pyautogui.click()

# abrir o Chrome
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome.exe')
pyautogui.press('enter')
pyautogui.moveTo(1056, 592)
pyautogui.click()
pyautogui.press('f11')


# abrir o YouTube
pyautogui.moveTo(795, 284)
pyautogui.click(clicks=1, interval=0.25)
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")

# Pesquisando a música
pyautogui.moveTo(761, 26)
pyautogui.click(clicks=1, interval=0.25)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")

# abrindo a música
pyautogui.moveTo(664, 187)
pyautogui.click(clicks=1, interval=0.25)
time.sleep(9)
pyautogui.press("f")
