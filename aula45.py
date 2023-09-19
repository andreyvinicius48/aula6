"""
faca um jogo para o usuario advinhar qual
a palavra secreta.
- voce vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuario digitar uma letra voce
vai conferir se a letra digitada esta
na palavra secreta.
  - se a letra digitada estiver na 
  palavra secreta; exiba a letra;
  -se a letra digitada estiver na 
  na palavra secreta; exiba *.
faca a contagem de tentativas do seu
usuario.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    os.system('clear')
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ' '
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

            print('palavra formada:', palavra_secreta)
            
        if palavra_formada == palavra_secreta:
            print('voce ganhou! parabens!')
            print('a palavra ', palavra_formada)
            print('tentativas', numero_tentativas)
            letras_acertadas = ''
            numero_tentativas = 0