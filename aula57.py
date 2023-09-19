"""
lista de listas e seus indices
"""
salas = [
    # 0        1
    ['maria', 'helena', ],  # 0
    # 0 
    ['elaine', ], # 1
    # 0      1      2
    ['luiz', 'joao', 'eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
     print(f'a sala e {sala}')
     for aluno in salas:
      print(aluno)
