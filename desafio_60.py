fatorial = int(input('Digite um numero que voce deseja ver o fatorial: '))
subtracao = 1
resultado_fatorial = 0
verdadeiro = False
soma = 0

while  not verdadeiro:
    if subtracao == 1:
        subtracao = fatorial - subtracao
        #print(f'VALOR DA SUBTRACAO {subtracao}')
        resultado_fatorial = fatorial * subtracao
        #print(f'VALOR DO RESULTADO {resultado_fatorial}')
    else:
        subtracao = subtracao - 1
        resultado_fatorial = resultado_fatorial * subtracao
        #print(f' O VALOR DO SEGUNDO RESULTADO E {resultado_fatorial}')
        if subtracao == 1:
            verdadeiro = True
        #print(f'O VALOR DA SEGUNDA SUBTRACAO E {subtracao}')
print(f'O fatorial de {fatorial} e {resultado_fatorial}')