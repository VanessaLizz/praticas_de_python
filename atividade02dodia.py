#Peça ao usuário um número. Dependendo se o número é par ou ímpar, exiba uma mensagem apropriada para o usuário.

numero_verificado = int(input("Digite um número: "))

resto = numero_verificado % 2

if resto == 0:
    print("O número escolhido é par")
else:
    print("O número escolhido é ímpar")

