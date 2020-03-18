def calcula_valor_devido(valor, meses, taxa):
    if meses == 0:
        return valor
    return valor*((1+taxa)**meses)