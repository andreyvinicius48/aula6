# desempacotamento em chamadas
# de metodos e funcoes
string = 'abcd'
lista = ['maria', 'helena', 1, 2, 3, 'eduarda']
tupla = 'python', 'e', 'legal'
salas = [
    # 0        1
    ['maria', 'helena', ],  # 0
    # 0 
    ['elaine', ], # 1
    # 0      1      2
    ['luiz', 'joao', 'eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('maria', 'helena', 1, 2, 3, 'eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, end='\n')
