frase=str(input('Digite uma frase qualquer: ')).upper()
a=frase.count('A')
print(f'Foi encontrado na frase {frase} um total de {a} letras: [A]')
posicao=frase.find('A')
print(f'Letra A encontrada pela primeira vez na posicao: [{posicao}]')
ultima_posicao=frase.rfind('A')
print(f'Letra A encontrada pela ultima vez na posicao: [{ultima_posicao}]')

