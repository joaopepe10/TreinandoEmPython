numero1=int(input('DIGITE O PRIMEIRO NUMERO: '))
numero2=int(input('DIGITE O SEGUNDO NUMERO: '))

if numero1>numero2:
    print(f'O PRIMEIRO NUMERO VENCEU!\nO NUMERO {numero1} E MAIOR')
elif numero2>numero1:
    print(f'O SEGUNDO NUMERO VENCEU!\nO NUMERO {numero2} E MAIOR')
elif numero1==numero2:
    print('AMBOS OS NUMEROS SAO IGUAIS')