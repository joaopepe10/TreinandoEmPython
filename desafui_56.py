import os

contador_de_mulheres = 0
media_do_grupo = 0
soma_idade = 0
homem_mais_velho = ''

for indice in range(0,4):
    nome = str(input('DIGITE SEU NOME: '))
    idade = int(input('DIGITE SUA IDADE: '))
    sexo = str(input('DIGITE SEU SEXO [M ou F]: ')).upper().strip()

    if sexo == 'F':
        if idade < 20:
            contador_de_mulheres = contador_de_mulheres + 1

    if indice == 0:
        mais_velho = idade
    else:
        if sexo == 'M':
            if idade > mais_velho:
                homem_mais_velho = nome

    soma_idade = idade + soma_idade
    media_do_grupo = soma_idade/4
    os.system("cls")
print(f'A media de idade grupo e de: {media_do_grupo}')
print(f'O nome do homem mais velho e : {homem_mais_velho.title()}')
print(f'Um total de {contador_de_mulheres} mulher(es) tem menos de 20 anos!')