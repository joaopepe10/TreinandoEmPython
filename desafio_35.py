a=int(input('Digite o valor da primeira parte do triangulo: '))
b=int(input('Digite o valor da segunda parte do triangulo: '))
c=int(input('Digite o valor da terceira parte do triangulo: '))

if a+b>c and a+c>b and b+c>c:
    print('Sim, da para fazer um triangulo com os valores informados!!!')
    if a == b == c:
        print('Que legal, este e um triangulo EQUILATERO!')
    elif a == b or a == c or  c == b:
        print('Que legal, este e um trinagulo ISOCELES!')
    elif a != b and a != c and c != b:
        print('Que legal, este e um triangulo ESCALENO!')

else:
    print('Vish, com essas medidas nao da para fazermos um triangulo, quem sabe na proxima!')
