termo = int(input('DIGITE O PRIMEIRO TERMO DA RAZAO: '))
razao = int(input('DIGITE A RAZAO DA P.A: '))
pa_termo = 0
flag = 11

while flag > 1:
    flag -= 1
    pa_termo = termo + (flag - 1) * razao
    print(f'{flag}° termo {pa_termo}')