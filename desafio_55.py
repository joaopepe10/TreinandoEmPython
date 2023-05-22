#maior = 0
#menor = 0
for i in range(0,5):
    peso = float(input('DIGITE SEU PESO: '))
    if i == 0:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f'O maior peso foi o {maior} e o menor foi o {menor}')
