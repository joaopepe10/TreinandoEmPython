sexo = 'MF' #declarei a variavel com os dois valores para fazer a verificacao do IN(dentro da string)
opc = 1 #comeco com a variavel em 1 pra fazer o programa rodar, e quando a verificacao do while for falsa, ela parar

while sexo in 'MF' and opc == 1: # enquanto sexo for M ou F and opcao == 1 o programa roda, se selecionar qualquer outro numero o programa para
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo in 'MF': #Verifica se o usuario digitou as letras pedidas e faz a verificacao se ele quer continuar ou nao no programa
        opc = int(input('DESEJA CONTINUAR ?\n[1]SIM\n[2]NAO\n'))
    while sexo != 'M' and sexo != 'F' and sexo != 'm' and sexo != 'f': # enquanto sexo for difente de todas essas opcoes, o programa diz que foi uma opcao incorreta digitada
        print('Opcao invalida, tente novamente')
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()