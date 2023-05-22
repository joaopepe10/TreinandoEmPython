import random
numero_aleatorio = random.randint(0,10)
palpites = 0
numero_da_sorte = int(input('Tente adivinhar o numero que o computador "pensou", numeros validos de 1 ate 10: '))

while numero_da_sorte != numero_aleatorio:
    numero_da_sorte = int(input('Vish voce errou, tente novamente: '))
    palpites += 1
print(f'Parabens, voce acertou,o numero que o computador pensou foi o {numero_aleatorio}, foram necessarios {palpites} palpites!')
