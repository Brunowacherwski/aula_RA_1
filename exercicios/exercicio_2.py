#Criar um programa que solicite ao usuário 2 listas com 5
#elementos cada. Como resultado, criar uma terceira lista que
#intercala os elementos das duas listas.

lista1 = []
lista2 = []
intercalada = []
for i in range(5):
    elementos1 = int(input("digite um numero (lista1)"))
    lista1.append(elementos1)
print(lista1)

for i in range(5):
    elementos2 = int(input("digite um numero(lista2)"))
    lista2.append(elementos2)
print(lista2)

for i in range(5):
    intercalada.append([lista1[i], lista2[i]])
print(intercalada)