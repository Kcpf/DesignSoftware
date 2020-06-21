"""
Existem diversas séries infinitas para o cálculo de pi. Abaixo está demonstrada uma série que permite calcular π/2. Desenvolva em Python uma função que recebe como argumento o número de elementos que serão usados na série e retorna o valor estimado de π.
2/1⋅2/3⋅4/3⋅4/5⋅6/5⋅6/7⋅8/7⋅8/9⋅⋯=π/2
Atenção, para esse exercício você deverá usar a estratégia apresentada para realizar o cálculo de π, outras estratégias não serão aceitas, e o valor retornado da função deve ser π (ou o valor aproximado alcançado pelo cálculo).

O nome da sua função deve ser PiWallis.
"""
def PiWallis(n):
    pi = 2
    
    for i in range(1, n+1):
        if i % 2 != 0:
            pi *= (i+1)/i
        else:
            pi *= i/(i+1)
     
    return pi