valor = int(input('DIGITE UM NUMERO DECIMAL QUE VOCE DESEJA CONVERTER: '))
opc=int(input('DIGITE UMA DAS OPCOES PARA CONVERSAO DE UM NUMERO DECIMAL PARA: \n\t\t[1] BINARIO\n\t\t[2] OCTAL \n\t\t[3] HEXADECIMAL\n'))

if opc == 1:
    binario = bin(valor)
    print(f'OPCAO ESCOLHIDA FOI  A CONVERSAO PARA BINARIO\nRESULTADO: {binario[2:]}')
elif opc == 2:
    octal = oct(valor)
    print(f'\033[43;30mOPCAO ESCOLHIDA FOI A CONVERSAO PARA OCTAL\033[m\n\033[41;97mRESULTADO: {octal[2:]}\033[m')
elif opc == 3:
    hexadecimal=hex(valor)
    print(f'OPCAO ESCOLHIDA FOI A CONVERSAO PARA HEXADECIMAL\nRESULTADO{hexadecimal[2:]}')
elif opc != 1 or 2 or 3:
    print('\033[30:41mOPCAO INVALIDA!\033[m')



