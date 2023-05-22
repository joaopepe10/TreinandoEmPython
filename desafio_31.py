km=float(input('Digite a distancia na qual voce quer percorrer: '))

if km<=200:
    print(f'O valor da passagem para a distancia de {km} quilometros e de R$ {km*0.5:.2f}')
else:
    print(f'O valor da passagem para a distancia de {km} quilometros e de R$ {km*0.45:.2f}')