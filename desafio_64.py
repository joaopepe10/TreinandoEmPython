num = 0
soma = 0
cont = 0
while num != 999:
    cont+=1
    num = int(input('DIGITE UM NUMERO: '))
    soma = soma + num
    if num == 999:
        soma = soma - 999
        cont = cont - 1

print(f'UM TOTAL DE {cont} foram digitados, e a soma de todos eles e: {soma}')