a = 80000
b = 200000
cont = 0

while a <= b:
    a += a * 0.03  # Crescimento de 3% da população A
    b += b * 0.015  # Crescimento de 1.5% da população B
    cont += 1

print(f"População de A: {a:.0f}")
print(f"População de B: {b:.0f}")
print(f"Para A passar B vai precisar de {cont} anos")
