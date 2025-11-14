#Crie um programa que peça ao usuário para inserir seu nome e sua idade. Imprima uma mensagem endereçada a ele informando o ano em que completará 100 anos

nome = ()
idade = 0
ano_atual = 2025

nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite a sua idade: "))

ano_de_100anos = ano_atual + idade_usuario
print(f"{nome_usuario}, você completará 100 anos em {ano_de_100anos}")