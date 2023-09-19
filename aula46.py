"""
listas em python
tipo list - mutavel
suporta varios valores da qualquer tipo
conhecimentos reutilizaveis - indices e fatimento
metodos uteis: append, isert,pop,del, clear, extend, +
"""
#        +01234
#       -54321
string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) # falsy
# print(lista, type (lista))
#       0   1        2              3     4
#      -5  -4        =3            -2    -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'maria'
print(lista)
print(lista[2], type(lista[1]))
