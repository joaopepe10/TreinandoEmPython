fatorial = int(input('Digite um numero no qual voce deseja calcular o fatorial: '))
resultado = 0
subtracao = 1

for i in range (0, fatorial-1):
    if i == 0:
        subtracao = fatorial - subtracao
        resultado = fatorial * subtracao
        print(subtracao)
    else:
        subtracao = subtracao - 1
        resultado = resultado * subtracao
        print(resultado)
print(f'O fatorial de {fatorial} e {resultado}')