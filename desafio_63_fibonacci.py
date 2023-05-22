a1 = 1
a2 = 1
numero_antigo = 0
termos = int(input('DIGITE QUANTOS TERMOS VOCE DESEJA VER DA SEQUENCIA DE FIBONACCI: '))
contador = 0
if termos >= 3:
    print(f'0, {a1}', end = ', ')
    while contador < termos - 2:
        print(a2, end = ', ')
        numero_antigo = a2
        a2 = a2 + a1
        a1 = numero_antigo
        contador += 1