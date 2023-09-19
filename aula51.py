"""
exercicio
exiba os indices da lista
maria
helena
luiz
"""
lista = ['maria', 'helena,' 'luiz']
lista.append('joao')


indices = range(len(lista))

for indice  in indices:
    print(indice, lista[indice], type(lista[indice]))
