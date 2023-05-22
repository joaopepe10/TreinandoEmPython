soma = 0
cont = 0
for c in range(1,500):
    multiplo = c*3
    if multiplo % 2 == 1 and multiplo < 500:
        soma = multiplo+soma
        cont =cont+1
print(f'A soma total e: {soma} dos {cont} numeros')
