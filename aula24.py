"""
exercicio
peca ao usuario para digitar seu nome
peca ao usario para digitar sua idade
se nome e idade forem digiitados:
    exiba
     seu nome e {nome}
     seu nome invertido e {nomme invertido}
     se nome contem 9ou nao espacos
     seu nome tem {n} letra
     a primeira letra do seu nome e {letra}
     a utima letra do seu nome e {letra}
se nada for digitado em nome ou idade:
   exiba "desculpe,, voce deixo campos vazios."
"""
nome = input('digite o seu nome ')
idade = input('ditige sua idade ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
