import string
import random

def gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ''
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas Aleatórias!")
    
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    
    senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    
    print("Senha gerada:", senha_gerada)

if __name__ == "__main__":
    main()
