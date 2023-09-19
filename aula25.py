"""
introducao ao try/exept
try -> tentar executar o codigo
except -> ocurreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    print('str', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
# if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'o dobro de {numero_str} e {numero_float *2:f}')
# else:
#   print('isso nao e um numero')