termo = int(input('DIGITE O PRIMEIRO TERMO DA RAZAO: '))
razao = int(input('DIGITE A RAZAO DA P.A: '))
pa_termo = 0

for c in range(1, 11):
    pa_termo = termo + (c - 1) * razao
    print(f'{c}° termo {pa_termo}')
 