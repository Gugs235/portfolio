import pyfiglet
from colorama import Fore, Style

# fontes:
# block
# starwars
# script
# standard
# lean

text = "Abacate"
ascii_art1 = pyfiglet.figlet_format(text, font="block")
print(f"\n{ascii_art1}")

ascii_art2 = pyfiglet.figlet_format(text, font="starwars")
print(f"\n{ascii_art2}")

ascii_art3 = pyfiglet.figlet_format(text, font="script")
print(f"\n{ascii_art3}")

ascii_art4 = pyfiglet.figlet_format(text, font="standard")
print(f"\n{ascii_art4}")

ascii_art5 = pyfiglet.figlet_format(text, font="lean")
print(f"\n{ascii_art5}")

# Juntando com o colorama
from colorama import init
init(autoreset=True)
text = "Helo, Mundo"
ascii_art6 = pyfiglet.figlet_format(text, font="slant")
print(Fore.CYAN + Style.BRIGHT + ascii_art6)

lista = ['Abacate', 'azedo', 'com', 'chocolate', 'maracuja']
ascii_art7 = pyfiglet.figlet_format(lista, font="slant")
print(Fore.RED + Fore.BLUE + Fore.WHITE + Fore.YELLOW + Fore.GREEN + Style.BRIGHT + ascii_art7)
