print('{:=^40}'.format(' JOKENPO '))
nome = str(input('DIGITE SEU NOME: ')).title()
opcao_humano = int(input('''DIGITE QUAL SUA OPCAO: 
\t[1] PEDRA
\t[2] PAPEL
\t[3] TESOURA
'''))

from random import randint
opcao_pc = randint(1,3)
print(opcao_pc)

if opcao_humano == 1 and opcao_pc == 2 or opcao_humano == 2 and opcao_pc == 1 or opcao_humano == 3 and opcao_pc == 2 or opcao_humano == 1 and opcao_pc == 3:
    print(f'Parabens {nome}, voce venceu!')
elif opcao_pc == 1 and opcao_humano == 2 or opcao_pc == 2 and opcao_humano == 1 or opcao_pc == 3 and opcao_humano == 2 or opcao_pc == 1 and opcao_humano ==3:
    print(f'Vish {nome}, voce perdeu para o computador, tente novamente!')
elif opcao_pc == opcao_humano:
    print(f'{nome}, voce acredita que deu empate?')
