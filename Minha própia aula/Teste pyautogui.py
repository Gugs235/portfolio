# # pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis

# # Encontrar a posição do mouse
# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr)
#         print('\b' * (len(positionStr) + 2))
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('\n')



import pyautogui
import time

time.sleep(1)
pyautogui.moveTo(19, 1055)

time.sleep(2)
pyautogui.click()

time.sleep(2)
pyautogui.write('Bloco de Notas', interval=0.25)

time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('Isso e so um teste!!!', interval=0.25)
time.sleep(2)
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('O triste e que o acento nao funciona', interval=0.25)

time.sleep(2)
pyautogui.moveTo(1571, 106)

time.sleep(2)
pyautogui.click()

time.sleep(2)
pyautogui.moveTo(979, 523)

time.sleep(2)
pyautogui.click()
