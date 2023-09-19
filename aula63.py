"""
argumentos nomeados e nao nomeados em funcoes python
argumento nomeado tem nome com sinal de legal
argumento nao nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # definicao
     print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, 2, z=5)

print(1, 2, 3, sep= '-')