# Exercício 2: Crie uma calculadora pré-programada para algum calculo

import pyautogui
import time


# # descobrir a posição
# for i in range(2): #caso precise marcar a posição de varios lugares
#     time.sleep(4)
#     posicao = pyautogui.position()
#     print(f"Posição é {posicao}")


pyautogui.PAUSE = 1.5

# abrir a calc 
pyautogui.hotkey("win", "r")
pyautogui.write("calc")
pyautogui.press('enter')

# fazer a conta
    # 75
pyautogui.moveTo(1266, 623)
pyautogui.click()
pyautogui.moveTo(1394, 732)
pyautogui.click()

    # X
pyautogui.moveTo(1672, 622)
pyautogui.click()

    # 6
pyautogui.moveTo(1530, 736)
pyautogui.click()

    # =
pyautogui.moveTo(1660, 925)
pyautogui.click()
