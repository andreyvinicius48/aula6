"""
closure e funcoes que retormam outras funcoes
"""


def criar_saudacao(saudacao):
    def saudar(nome):
     return f'{saudacao,} {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('bom noite')
falar_bom_noite= criar_saudacao('bom dia' )

print(falar_bom_dia('luiz'))
print(falar_bom_noite('luiz'))

for nome in ['marcia', 'joana', 'luiz']:
   print(falar_bom_dia(nome))
   print(falar_bom_noite(nome))