def numero(num1, num2):
    produto = num1 * num2

    if produto <= 1000:
        return produto
    else:
        return num1 + num2
    
resultado = numero(20, 30)
print(f"o resultado é: {resultado}")
resultado2 = numero(500, 7)
print(f"o resultado é: {resultado2}")
resultado3 = numero(75, 20)
print(f"o resultado é: {resultado3}")
resultado4 = numero(5, 9)
print(f"o resultado é: {resultado4}")

