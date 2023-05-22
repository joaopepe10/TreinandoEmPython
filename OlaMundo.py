#import math

#angulo=float(input('Digite qualquer angulo: '))
#x=math.radians(angulo)
#seno=math.sin(x)
#cosseno=math.cos(x)
#tangente=math.tan(x)

#print(f'O valor do seno e {seno}\nO valor do cosseno {cosseno}\nO valor da tangente {tangente}')

import random

a=str(input('Digite o nome do primeiro aluno: '))
b=str(input('Digite o nome do segundo aluno: '))
c=str(input('Digite o nome do terceiro aluno: '))
d=str(input('Digite o nome do quarto aluno: '))
lista=[a,b,c,d]
random.shuffle(lista)

print(lista)