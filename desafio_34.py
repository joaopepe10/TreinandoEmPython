salario=float(input('Digite seu salario e vamos ver quanto sera seu aumento: '))

if salario>1250:
    print(f'O valor do seu salario teve um aumento de 10%, voce recebia {salario}, a partir de agora voce recebera R$ {salario*1.1:.2f}')
else:
    print(f'O valor do seu salario teve um aumento de 15%, voce recebia {salario}, a partir de agora voce recebera R$ {salario*1.15:.2f}')