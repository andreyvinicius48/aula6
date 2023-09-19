# exercicios com funcoes

# crie uma funcao que multipica todos os argomentos
# nao nomeados recebidos 
# retorno o total para uma variavel e mostre o valor
# da variavel.
def multiplicar(*args):
    total = 0
    for numero in args:
        total *= numero
        return total
    
multiplicacao = multiplicar(10,2,3,4,5)
print(multiplicacao)


# crie uma funcao fala se um numero e par ou impar.
# retorne se o numero e por ou impar.
def par_impar(numero):
    mltiplo_de_dois = numero % 2 ==  0
    
    if multiplicacao:
        return f'{numero} e par'
    return f'{numero} e impar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))