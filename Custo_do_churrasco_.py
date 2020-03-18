total = 0
for c in open("churras.txt", "r", encoding="utf8").readlines():
    lista = str(c).split(",")
    total += float(lista[1])*float(lista[2])
print(total)

