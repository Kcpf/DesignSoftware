def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    elif 11<idade<=17:
        return "adolescente"
    else:
        return "adulto"