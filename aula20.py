# operadores logicas
# and (e or (ou) nnot (nao)
# and - todas as condicoes precisam ser 
# verdadeiras.
# se qualquer valor for considerado falso,
# a expressao inteira sera avaliada naquele valor
# sao consiferados falsy (que vc ja viu)
# 0 0.0  '' false
# tambem exiiste o tipo none que e 
# usado para representar um nao valor
# entrada = input('[E]ntrar [S]air:')
# senha_digitada = input('senha')

# senha_permitida = '123456'
# # if true
# #  ...
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('entrar')
# else:
#     print('sair')
# avaliacao de cutto ciruito
print(True and False and True)
print(True and 0 and True)
