valor_casa=float(input('Digite o valor da casa que voce deseja comprar: '))
salario=float(input('Digite o valor do seu salario: '))
tempo=int(input('Digite o prazo que voce deseja pagar em anos: '))
salario_com_desconto=salario*0.3
meses=tempo*12
mensalidade=valor_casa/meses

if mensalidade<=salario_com_desconto:
    print('\033[97;42mEMPRESTIMO APROVADO!\033[m')
    print(f'Voce teve o emprestivo aprovado, de acordo com seu salario de R$ {salario}, voce conseguira quitar sua casa em apenas {meses} meses, pagando apenas R${mensalidade:.2f} por mes')
else:
    print('\033[30;41mEMPRESTIMO NEGADO!\033[m')
    print(f'Voce nao teve o emprestimo autorizado pelo banco, com o seu salario de R${salario}, voce conseguiria pagar o emprestimo se a mensalidade fosse R${mensalidade:.2f} em apenas {meses} meses.')