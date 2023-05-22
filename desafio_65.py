opc = 's'
maior = menor = soma = cont = 0
while  opc != 'n':
    num = int(input('DIGITE UM NUMERO: '))
    opc = str(input('DESEJA CONTINUAR ? [S/N] ')).lower()
    if cont == 0:
        maior = num
        menor = num
    else:
        if maior > num:
            maior = num
        if menor < num:
            menor = num
    cont+=1
    soma+=num
print(f'Voce digitou {cont} numeros, a media entre eles e de {soma/cont}\nO maior entre os numero e {maior}\nO menor entre os numero e {menor}')