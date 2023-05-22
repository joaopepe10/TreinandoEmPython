numero=int(input('Digite um valor de 0 a 9999: '))
print(f'O valor em milha e: {numero//1000}\nO valor em centena e: {numero//100%10}\nO valor em dezena e: {numero//10%10}\nO valor em unidade e: {numero%10}')

