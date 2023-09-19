"""
flag (bandeira) - marcar um local
nome = nao valor
is e is not = e ou nao e (tipo, valor, identidade)
id = identidade
"""
condicao = False
passou_no_if = None

if condicao:
   passou_no_if = True
   print('faca algo')
else: 
   print('nao faca algo')


if passou_no_if is None:
   print('nao passou no if')
else:
   if passou_no_if is not None:
      print('passou no if')