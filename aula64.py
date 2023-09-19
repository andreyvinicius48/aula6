"""
valores padrao para paramentros
ao definir uma funcao, os para podem
ter valores pardao, caso o valor nao seja 
enviado para o parametro, o valor padrao sera
usado.
refatorar: editar o seu codigo.
"""


def soma(x, y, z=None):
      if z is not None:
       print(f'{x=} {y=} {z=}', x + y + z)
      else:
       print(f'{x=} {y=} {z=}', x + y )
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)