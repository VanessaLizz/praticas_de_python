a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

resultado_lista = []
resultado = {}

for i in range(len(a)):
    valor = a[i]

    if valor in b:
        resultado_lista.append(valor)

        if valor in resultado:
            resultado[valor] += 1
        else:
            resultado[valor] = 1

print("Os números contidos nas duas listas são:", resultado_lista)
print("A quantidade de cada item na lista é:", resultado)
