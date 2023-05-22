nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
media=(nota1+nota2)/2

if media < 5.0:
    print(f'Poxa, voce tirou {media} na media, infelizmente voce \033[40;41mREPROVOU\033[m, ate ano que vem de novo!')
elif media >= 5.0 and media <= 6.9:
    print(f'Vish, voce tirou {media} na media, portanto esta de \033[40;35mRECUPERACAO\033[m, a prova sera dia 07/02/2023, boa sorte!')
elif media >= 7.0:
    print(f'Paraaabens, voce tirou {media} na media, e voce foi \033[107;42mAPROVADO\033[m, boas ferias!')