#------ATIVIDADE 02------

camisa = float(input('Digite o preço da camisa: '))
desconto1 = ((camisa*13)/100)
valor_com_desconto = camisa - desconto1
print(f'O valor do desconto é: R${desconto1:.0f} e o valor final é: R${valor_com_desconto:.0f}')