import pyautogui

# pergunta2 = pyautogui.alert(text='Qual é a capital da França?', title='Pergunta 2', button='OK')

# pergunta3 = pyautogui.confirm(text='Qual é a capital da França?', title='Pergunta 3', buttons=['OK', 'Cancel'])

# pergunta4 = pyautogui.password(text='Qual é a capital da França?', title='pergunta4', default='Digite a senha', mask='*')

pergunta1 = pyautogui.prompt("Qual é a capital da França?", "Pergunta 1")
if pergunta1.lower() == "paris":
    pyautogui.alert("Resposta correta!")
else:
    pyautogui.alert("Resposta errada!")


pergunta2 = pyautogui.prompt("Em que ano a 2° Guerra Mundial acabou?", "Pergunta 2")
if pergunta2.lower() == "2 de setembro de 1945":
    pyautogui.alert("Resposta correta!")
elif pergunta2 == "02/09/1945":
    pyautogui.alert("Resposta correta!")
elif pergunta2 == "2/9/1945":
    pyautogui.alert("Resposta correta!")
else:
    pyautogui.alert("Resposta errada!")

pergunta3 = pyautogui.prompt("Em que ano a 1° Guerra Mundial começou?", "Pergunta 3")
if pergunta2.lower() == "2 de setembro de 1945":
    pyautogui.alert("Resposta correta!")
elif pergunta2 == "02/09/1945":
    pyautogui.alert("Resposta correta!")
elif pergunta2 == "2/9/1945":
    pyautogui.alert("Resposta correta!")
else:
    pyautogui.alert("Resposta errada!")
