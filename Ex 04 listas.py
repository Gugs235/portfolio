print("\n")
# uma lista de duas temperaturas por mes
jan = [20, 25]
fev = [21, 27]
mar = [40, 22]
abr = [50, 52]
mai = [51, 37]
jun = [70, 41]
jul = [55, 60]
ago = [71, 90]
set = [33, 19]
out = [10, 9]
nov = [6, 91]
dez = [69, 53]

# uma lista com todas as outras listas
# média das temperaturas anual
temp = jan
temp.extend(fev)
temp.extend(mar)
temp.extend(abr)
temp.extend(mai)
temp.extend(jun)
temp.extend(jul)
temp.extend(ago)
temp.extend(set)
temp.extend(out)
temp.extend(nov)
temp.extend(dez)

media = (sum(temp)/12)
temp.sort()

print(temp)
print(f"a média da temperatura anual foi de {media:.2f}")
print(max(temp))
print(min(temp))
