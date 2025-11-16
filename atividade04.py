#Escreva um programa que retorne uma lista contendo apenas os elementos comuns às duas listas (sem duplicatas). Certifique-se de que seu programa funcione com duas listas de tamanhos diferentes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []


for item in a:
    if item in b and item not in c:
        c.append(item)


print(c)

#lista 02

x = [4, 9, 2, 9, 1, 4, 7, 6]
y = [5, 2, 7, 2, 8, 1]
z = []

for item in x:
    if item in y and item not in z:
        z.append(item)
print(z)