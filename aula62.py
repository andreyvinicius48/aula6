"""
introducao as funcoes (def) em python
funcoes sao trechos de codigo usados para
repilcar determinada acao ao longo do seu codigo.
elas podem receber valores para parametros (argumentos)
e retornar um valor especifico
por padrao, funcoes python retornam none (nada).
"""


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#    print(a, b, c)
    

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()