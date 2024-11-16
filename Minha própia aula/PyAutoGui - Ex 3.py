# Exercício 3: Aumente o volume no maximo, abra o Google Chrome na tela inicial, 
# entre no YouTube e abra a música: "You Are Good - Israel & New Breed"

import pyautogui
import time
# # descobrir a posição
# for i in range(2): #caso precise marcar a posição de varios lugares
#     time.sleep(4)
#     posicao = pyautogui.position()
#     print(f"Posição é {posicao}")

# Pausa padrão entre comandos para dar tempo ao programa
pyautogui.PAUSE = 1.5

# aumentar o volume
pyautogui.moveTo(1193, 751)
pyautogui.click()
pyautogui.moveTo(1302, 700)
pyautogui.click()

# abrir o Chrome
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome.exe')
pyautogui.press('enter')
pyautogui.moveTo(945, 306)
pyautogui.click()

# abrir o YouTube
pyautogui.moveTo(581, 64)
pyautogui.click(clicks=1, interval=0.25)
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")

# Pesquisando a música
pyautogui.moveTo(704, 150)
pyautogui.click(clicks=1, interval=0.25)
pyautogui.write("https://youtu.be/5KiQDoWo5t4?si=pB5SpqYDdZ2O78zV", interval=0.25)
pyautogui.press("enter")

# abrindo a música
pyautogui.moveTo(622, 365)
pyautogui.click(clicks=1, interval=0.25)
