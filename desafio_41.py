from datetime import  datetime

nas = int(input('Digite o ano que o atleta nasceu: '))
ano_atual = datetime.now().year
idade = ano_atual - nas

if idade <= 9 and idade >0:
    print(f'Voce tem {idade}, portanto sua categoria e MIRIM!')
elif idade >9 and idade <= 14:
    print(f'Voce tem {idade}, portanto sua categoria e INFANTIL!')
elif idade >14 and idade <=19:
    print(f'Voce tem {idade}, portanto sua categoria e JUNIOR!')
elif idade <= 25:
    print(f'Voce tem {idade}, portanto sua categoria e SENIOR!')
elif idade > 25:
    print(f'Voce tem {idade}, portanto sua categoria e MASTER!')
else:
    print('Voce ainda nem nasceu, esta um pouco adiantado em!')