valor_pago = float(input('DIGITE O VALOR DO PRODUTO: '))
opc = int(input('''DIGITE A FORMA DE PAGAMENTO: 
\t[1] A VISTA/CHEQUE 10% DE DESCONTO
\t[2] A VISTA NO CARTAO 5% DE DESCONTO
\t[3] EM ATE DUAS VEZES SEM JUROS
\t[4] 3 VEZES OU MAIS NO CARTAO, 20% DE JUROS
'''))

if opc == 1:
    desconto = valor_pago * 0.1
    desconto = valor_pago - desconto
    print(f'O valor do produto e de R$ {valor_pago}, como voce escolheu a opcao de pagamento a vista, voce tera 10% de desconto, dando um total de R$ {desconto}')
elif opc == 2:
    desconto = valor_pago * 0.05
    desconto = valor_pago - desconto
    print(
        f'O valor do produto e de R$ {valor_pago}, como voce escolheu a opcao de pagamento a vista no carta, voce tera 5% de desconto, dando um total de R$ {desconto}')
elif opc == 3:
    print(f'Como voce escolheu parcelar sem juros, o valor do produto continua o mesmo, o valor de cada parcela fica em R${valor_pago/2:.2f}')
elif opc == 4:
    print(f'Como voce escolheu parcelar de 3 vezes ou mais, voce tera um acrescimo de 20% de juros no valor total do produto, produto vale R${valor_pago}, agora o produto vale R${valor_pago*1.2}')
