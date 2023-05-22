dia = int(input('DIGITE O DIA QUE VOCE NASCEU: '))
mes = int(input('DIGITE O MES QUE VOCE NASCEU: '))
ano = int(input('DIGITE O ANO QUE VOCE NASCEU: '))

from datetime import datetime,timedelta

data_nascimento = datetime(year=ano, month=mes, day=dia)
hoje = datetime.now()
diferenca = hoje - data_nascimento
diferenca = diferenca.days
if diferenca >=6570:
    print(f'Vejo aqui que voce tem {diferenca/365:.0f} anos, ja passou da hora de voce se alistar!')
elif diferenca <6570:
    print(f'Vejo aqui que voce tem {diferenca/365:.0f} anos, faltam {18-diferenca/365:.0f} ano para voce se alistar!')

#ano_passado = hoje