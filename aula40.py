
produto1 = [ "maçã", 10, 0.30]
produto2 = [ "pera", 5, 0.75]
produto3 = [ "kiwi", 4, 0.98]
compras = [ produto1, produto2, produto3]
for e in compras:
 print("Produto: %s" % e[0])
print("Quantidade: %d" % e[1])
print("Preço: %5.2f" % e[2])
compras = [ ]
while True:
 produto = input("Produto: ")
 if produto == "fim":
   break
quantidade = int(input("Quantidade: "))
preço = float(input("Preço: "))
compras.append([produto, quantidade, preço])
soma = 0.0
for e in compras:
 print("%20s x%5d %5.2f %6.2f" % (e[0],
 e[1],e[2],
 e[1] * e[2]))
soma += e[1] * e[2]
print("Total: %7.2f" % soma)