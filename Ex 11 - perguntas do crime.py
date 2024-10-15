# telefonou para vitima?
# esteve no local do crime?
# esteve no local do crime?
# devia para a vitima?
# ja trabalhou com a vitima?

p1 = str(input("Telefonou para vitima? "))
p2 = str(input("Esteve no local do crime? "))
p3 = str(input("Mora perto da vitima? "))
p4 = str(input("Devia para a vitima? "))
p5 = str(input("Ja trabalhou com a vitima? "))

cont = 0

if p1 == "s" or p1 == "S" or p1 == "sim" or p1 == "Sim" or p1 == "SIM":
    cont = cont + 1
if p2 == "s" or p2 == "S" or p2 == "sim" or p2 == "Sim" or p2 == "SIM":
    cont = cont + 1
if p3 == "s" or p3 == "S" or p3 == "sim" or p3 == "Sim" or p3 == "SIM":
    cont = cont + 1
if p4 == "s" or p4 == "S" or p4 == "sim" or p4 == "Sim" or p4 == "SIM":
    cont = cont + 1
if p5 == "s" or p5 == "S" or p5 == "sim" or p5 == "Sim" or p5 == "SIM":
    cont = cont + 1

# se não = inocente
# 2 sim = suspeita
# 3 e 4 = cumplice
# 5 sim = assassino

print(cont)

if cont <= 1:
    print("Inocente")
if cont == 2:
    print("Suspeita")
if cont >= 3 and cont <= 4:
    print("Cumplice")
if cont == 5:
    print("Assassino")
