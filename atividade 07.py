#Dada uma lista em Python, escreva um programa para adicionar todos os seus elementos a um conjunto dado.

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(f'O resultado do conjunto é: {sample_set}')


#Verifique se set1é um subconjunto de set2. Escreva um código para retornar Truese cada elemento em subset_settambém estiver presente em main_set.

subset_set = {10, 20}
main_set = {10, 20, 30, 40}

is_subset = subset_set.issubset(main_set)
print(f"O seguinte dado: {subset_set} é um subconjunto de {main_set}? {is_subset}")
