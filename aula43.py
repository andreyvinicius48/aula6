"""
interavel -> str, range, etc (__iter__)
interador -> quem sabe entregar um valor por vez 
next -> me entregue o proximo valor 
iter -> me entregue seu iterador
"""
# for nletra in texto
texto = 'luiz' # iteravel
# Iterator = iter(texto) # iterator

# while True:
#     try:
#       letra = next(Iterator)
#       print(letra)
#     except StopIteration:
#         break
for letra in texto:
    print(letra)