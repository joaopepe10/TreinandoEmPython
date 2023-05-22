ano=int(input('Digite qualquer ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este e um ano bissexto!')
else:
    print('Este nao e um ano bissexto!')