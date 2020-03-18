distancia = float(input())
if distancia <= 200:
    print("{:.2f}".format(distancia*0.5))
else:
    print("{:.2f}".format(100 + (distancia-200)*0.45))
