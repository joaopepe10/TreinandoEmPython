peso=float(input('DIGITE SEU PESO: '))
altura=float(input('DIGITE SUA ALTURA: '))

imc=peso/(altura*altura)
print(f'O SEU IMC ESTA EM: {imc:.1f}')
if imc < 18.5:
    print('VOCE ESTA ABAIXO DO PESO, BORA ENTRAR NA ACADEMIA SEU FRANGO!')
elif 18.5 <= imc < 25:
    print('VOCE ESTA COM O PESO IDEAL, CONTINUE ASSIM!')
elif 25 <= imc < 30:
    print('VOCE ESTA COM SOBREPESO, BORA ENTRAR NA ACADEMIA O QUANTO ANTES!')
elif 30 <= imc < 40:
    print('VOCE ESTA OBESO, SUA SUADE CORRE RISCO, PROCURE UM MEDICO JA!')
elif imc >= 40:
    print('VOCE ESTA COM OBESIDADE MORBIDA, PROCURE UM MEDICO O QUANTO ANTES, ANTES QUE SEJA TARDE!')