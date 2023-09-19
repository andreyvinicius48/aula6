"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco e r$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d e %08x' % ( 1500, 1500))