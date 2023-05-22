from datetime import datetime
import  os
cont_maior_de_idade = 0
cont_menor_de_idade = 0
hoje = datetime.now()

for i in range(0,7):
    dia = int(input('DIGITE O DIA QUE VOCE NASCEU: '))
    mes = int(input('DIGITE O MES QUE VOCE NASCEU: '))
    ano = int(input('DIGITE O ANO QUE VOCE NASCEU: '))
    data_nascimento = datetime(year=ano, month=mes, day=dia)
    diferenca = hoje - data_nascimento
    diferenca = diferenca.days
    if diferenca >= 7665:
        cont_maior_de_idade = cont_maior_de_idade + 1
    if diferenca < 7665:
        cont_menor_de_idade = cont_menor_de_idade + 1
    os.system("cls")


print(f'''Um total de {cont_maior_de_idade} pessoas sao maiores de idade!
Um total de {cont_menor_de_idade} pessoas sao menores de 21 anos!''')
