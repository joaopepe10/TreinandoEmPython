from time import sleep

print('\033[31m{:=^40}'.format('\033[31mSEQUENCIA'))
sleep(1)
print('{:=^40}'.format('DE'))
sleep(1)
print('{:=^40}'.format('FIBONACCI'))
sleep(1)
quantidade_de_termos = int(input('\033[35m\nDIGITE QUANTOS  TERMOS DESEJA VER: '))
t1 = 0
t2= 1
contador = 3
if quantidade_de_termos == 2:
    print(f'\033[34m{t1} - {t2} - ',end = '')

elif quantidade_de_termos == 1:
    print(t1,end=' -')

elif quantidade_de_termos > 2:
    sleep(0.5)
    print(f'\033[34m{t1} - ',end='')
    sleep(0.5)
    print( f'{t2} - ', end='')
    while contador <= quantidade_de_termos:
        t3 = t2 + t1
        sleep(0.5)
        print(f'{t3} - ',end = '')
        contador += 1
        t1 = t2
        t2 = t3
print(' FIM')

# 0 - 1 - 1 - 2 - 3 - 5 - 8
#                   t1  t2  t3