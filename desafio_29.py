vel=int(input('Digite a velocidade que voce passou no radar: '))

if vel>80:
    print('Voce ultrapassou os limites de velocidade, sua multa e de: R$ {}'.format((vel-80)*7))
else:
    print('Velocidade maxima permitida, voce e um otimo condutor, continue assim!!!')