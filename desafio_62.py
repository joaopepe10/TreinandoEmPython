primeiro_termo = int(input('DIGITE O PRIMEIRO TERMO DA RAZAO: '))
razao = int(input('DIGITE A RAZAO DA P.A: '))
termo = primeiro_termo
contador = 1
saida = 11
termo_extra = 1

while contador < saida and termo_extra != 0:
    termo = primeiro_termo + (contador - 1) * razao
    print(f'{contador}° termo = {termo}', end=' ')
    contador += 1
    if contador >= saida:
        termo_extra = int(input('\nDesja adicionar quantos termos a mais: '))
        termo = termo + termo_extra
        saida = saida + termo_extra
        if termo_extra != 0:
            print(f'{contador}° termo = {termo + ermo_extra - termo_extra}', end=' ')
print('Programa finalizado com sucesso!')