numero_cadastro = int (input("Informe o número do cadastro do vendedor ==> "))
salario_fixo = float (input("Informe seu salário fixo ==> "))
total_vendas = float (input("Informe seu total de vendas em reais ==> "))
perc_comissao = float (input("Informe seu percentual de comissão sobre as vendas ==> "))

comissao = total_vendas * perc_comissao / 100
salario_final = salario_fixo + comissao

print(f"Cadastro: {numero_cadastro}")
print(f"Salário fixo: {salario_fixo:,.2f}")
print(f"Valor da comissão: {comissao:,.2f}")
print(f"Salário: {salario_final:,.2f}")