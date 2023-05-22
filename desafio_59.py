primeiro_valor = float(input('Digite o primeiro valor: '))
segundo_valor = float(input('Digite o sendo valor: '))
saida = 0
resultado = 0

while saida != 5:
    saida = int(input('Digite uma opcao: \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Numeros \n[5] Sair do programa\n'))
    if saida == 1:
        resultado = primeiro_valor + segundo_valor
        print(f'A soma de {primeiro_valor} e {segundo_valor} e {resultado}')
    elif saida == 2:
        resultado = primeiro_valor * segundo_valor
        print((f'A multiplicacao de {primeiro_valor} e {segundo_valor} e {resultado}'))
    elif saida == 3:
        if primeiro_valor > segundo_valor:
            print(f'O maior numero e {primeiro_valor}.')
        elif segundo_valor > primeiro_valor:
            print(f'O maior numero e {segundo_valor}.')
        elif primeiro_valor == segundo_valor:
            print(f'Ambos os numeros sao iguais, portanto nao ha um maior.')
    elif saida == 4:
        primeiro_valor = float(input('Digite novamente o primeiro valor: '))
        segundo_valor = float(input('Digite novamente o segundo valor: '))
print('Programa finalizado com sucesso!')
