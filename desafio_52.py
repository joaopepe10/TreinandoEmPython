numero = int(input('DIGITE UM NUMERO PARA VERIFICAR SE ELE E OU NAO PRIMO: '))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f'{numero} nao e primo!')
            break
    print(f'{numero} e primo!')
elif numero == 1:
    print(f'{numero} nao e primo!')
elif numero == 0:
    print(f'{numero} nao e primo!')
else:
    print('Opcao invalida')