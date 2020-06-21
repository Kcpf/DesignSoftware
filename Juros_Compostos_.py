"""
Escreva uma função que calcula o valor devido ao final de um empréstimo. 
Os argumentos de entrada da função serão: valor emprestado, número de meses e taxa de juros. 
Atenção: usar juros compostos para calcular o valor devido.

O nome da sua função deve ser calcula_valor_devido.
"""

def calcula_valor_devido(valor, meses, taxa):
    if meses == 0:
        return valor
    return valor*((1+taxa)**meses)