"""
cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aposnta para o mesmo valor na memoria (mutavel)
"""
lisa_a = ['luiz', ' maria' , 1, True, 1.2]
lisa_b = lisa_a.copy()

lisa_a[0] = 'qualqueer coisa'
print(lisa_b)
print(lisa_b)
