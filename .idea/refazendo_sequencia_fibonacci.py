termos = int(input('DIGITE QUANTOS TERMOS VOCE DESEJA VER: '))
contador = 3
t1 = 0
t2 = 1
t3 = 1
if termos < 3:
    print(f'{t1} - {t2}')
else:
    print(f'{t1} - {t2}',end=' - ')

while contador < termos + 1:
    print(t3,end=' - ')
    contador+=1
    t1 = t2
    t2 = t3
    t3 = t2 + t1

