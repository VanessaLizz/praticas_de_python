#Considere uma lista, por exemplo, esta:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# e escreva um programa que imprima todos os elementos da lista que sejam menores que 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista_menor_que_5 = []

for i in a:
    if i < 5:
        lista_menor_que_5.append(i)
print(f"Os números menores que 5 da lista são: {lista_menor_que_5}")