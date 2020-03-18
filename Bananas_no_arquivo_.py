cont = 0
file = open("macacos-me-mordam.txt", "r")
lines = file.readlines()
for line in file:
    line = line.strip()
    for l in line.split():
        if l.upper() == "BANANA":
            cont += 1
print(cont)