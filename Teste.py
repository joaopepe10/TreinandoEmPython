'''import random
p = random.randint(0,5)
e = int(input('Adivinhe o Numero que a Máquina Pensou de 0 a 5:'))
if p == e:
    print('Droga você Acertou Parabens!')
    print('Jogue Novamente')
else:
    print(f'Você errou o numero era {p}')
    print('Tente Novamente')
'''

a, b = 0, 1
termos = int(input('DIGITE QUANTOS TERMOS VOCE DESEJA VER: '))
for i in range(termos):
    print(a, end = ' -> ')
    a, b = b, a + b
print('FIM')