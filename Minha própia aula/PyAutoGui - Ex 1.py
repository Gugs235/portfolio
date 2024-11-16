import pyautogui
import time

# # descobrir a posição
# for i in range(2): #caso precise marcar a posição de varios lugares
#     time.sleep(4)
#     posicao = pyautogui.position()
#     print(f"Posição é {posicao}")


# Pausa padrão entre comandos para dar tempo ao programa
pyautogui.PAUSE = 0.5

# abrir o paint
pyautogui.hotkey('win', 'r')
pyautogui.write('mspaint')
pyautogui.press('enter')

pyautogui.hotkey('alt', 'space')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

# selecionar a ferramenta
pyautogui.press('alt')
pyautogui.press('h')
pyautogui.press('s')
pyautogui.press('h')
for i in range(3):
    pyautogui.press('right')
pyautogui.press("enter")

# desenhar o retangulo
pyautogui.moveTo(98, 208)
pyautogui.mouseDown()
pyautogui.dragTo(221, 379)
pyautogui.mouseUp()
pyautogui.click()

# selecionar a ferramenta
pyautogui.press('alt')
pyautogui.press('h')
pyautogui.press('s')
pyautogui.press('h')
pyautogui.press('left')
pyautogui.press("enter")

# desenhar o circulo
pyautogui.moveTo(321, 208)
pyautogui.mouseDown()
pyautogui.dragTo(542, 406)
pyautogui.mouseUp()
pyautogui.click()
