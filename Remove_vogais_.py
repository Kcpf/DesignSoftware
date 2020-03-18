def remove_vogais(s):
    string = ""
    vogais = ["a", "e", "i", "o", "u"]
    for c in s:
        if c not in vogais:
            string += c
    return string