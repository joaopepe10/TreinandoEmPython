num1=int(input('DIGITE O PRIMEIRO NUMERO: '))
num2=int(input('DIGITE O SEGUNDO NUMERO: '))
num3=int(input('DIGITE O TERCEIRO NUMERO: '))

if num1>num2:
    if num1>num3:
        print(f'Dentre os tres numeros, o maior e o: {num1}')
if num2>num1:
    if num2>num3:
        print(f'Dentre os tres numeros, o maior e o: {num2}')
if num3>num1:
    if num3>num2:
        print(f'Dentre os tres numeros, o maior e o: {num3}')