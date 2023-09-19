"""
listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis:
    append - adiciona um item ao final
    insert - adiciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena lista
create read update delete
criar, ler, alterar, apagar = lista[1] crud
"""
lista_a = [1, 2, 3,]
lista_b = [ 4, 5, 6 ]
lista_c = lista_a + lista_b
lista_d = lista_a .extend(lista_b)
print(lista_d)
