"""
enumerate - enumera iteraveis (injdices)
"""
lista = ['maria', 'helena', 'luiz']
lista.append('joao')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)


for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')