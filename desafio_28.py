num1=int(input('Tente acertar o numero que o computador pensou, de 0 ao 5.\n\t\t\tNumero escolhido: '))
import random
num2=random.randint(0,5)

if num1==num2:
    print(f'Numero que o computador pensou foi o {num2}')
    print('\t\t\tParabens, voce acertou!!!')
else:
    print(f'Numero que o computador pensou foi o {num2}')
    print('\t\t\tParabens, voce e um merda, voce errou!!!')