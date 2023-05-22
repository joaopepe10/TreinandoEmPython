nome=str(input('Digite uma frase: '))
quantidade=nome.count(input('Digite a letra na qual voce deseja verificar: ')) #verifica a letra desejada e quantas vezes ela aparece
arm=nome.find(input('Digite o que voce procura na palavra: ')) #Faz a busca de onde esta a palavra e retorna a posicao da mesma no vetor/lista
print(f'O numero de vezes que a letra se repete e de {quantidade} vezes ')
print(f'Encontrado na posicao: {arm}')
teste=nome.title() #faz com que a primeira letra de cada frase seja mudada para maiscula
print(teste)
lista=nome.split()
print(lista)