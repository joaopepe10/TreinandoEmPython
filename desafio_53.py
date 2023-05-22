frase = str(input('DIGITE UM FRASE: ')).strip()
frase.upper()
tam = len(frase) - frase.count(' ')
for i in range(0, tam):
    frase.replace(' ', '')
    if frase.replace(' ', '')[i].upper() == frase.replace(' ', '')[:tam-i].upper():
        print('E UM PALINDROMO')

