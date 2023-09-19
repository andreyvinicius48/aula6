"""
liostas em python 
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis;
    append, insert, pop, del, clear, extend, +
create read upadate delete 
cria, ler, alterar, apagar + lista[i] (crud)
"""
lista = [10, 20, 30, 40, 50, 60]
# numero = lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
ultimo_valor = lista.pop()
lista.append(60)
lista.append('BBB')
ultimo_valor = lista.pop()
print(lista, 'removido', ultimo_valor)