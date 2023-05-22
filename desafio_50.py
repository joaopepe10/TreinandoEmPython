soma_par = 0

for c in range (1,7):
    num1 = int(input(f'DIGITE O {c}° numero: '))
    if num1 % 2 == 0:
        soma_par = num1+soma_par
print(soma_par)