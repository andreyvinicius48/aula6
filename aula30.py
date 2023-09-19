"""
repeticoes
while (enquanto)
executa um acao enquanto uma condicao for verdadeira
loop infinito -> quando um codigo nao tem fim
"""
condicao = True

while condicao:
    nome = input('qual o seu nome: ')
    print(f'seu nome e {nome}')

    if nome == 'sair':
      break

print('acabou')
