# for - define cor do texto
# back - cor do fundo
# style - define o estilo - negrito,sublinhado
# reset - reseta a cor e o estilo

from colorama import Fore, Style, init, Back
init()
print(Fore.RED + "Vermelho")
print(Fore.GREEN + "Verde")
print(Fore.BLUE + "Azul")
print(Style.RESET_ALL + "Texto padrão")
print(Back.RED + ' Texto com fundo AMARELO ')
