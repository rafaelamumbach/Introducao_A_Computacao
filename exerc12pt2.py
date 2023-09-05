numero_mat = int (input("Informe o número da matrícula do vendedor ==> "))
salario_fixo = float (input("Informe seu salário fixo ==> "))
total_vendas = float (input("Informe seu total de vendas em reais ==> "))
num_carros = float (input("Informe o número de carros vendidos ==> "))
perc_comissao = float (input("Informe sua comissão sobre as vendas ==> "))

salario_final = salario_fixo + total_vendas * 1 / 100 + num_carros * perc_comissao

print(f"Matrícula: {numero_mat}")
print(f"Salário: {salario_final:,.2f}")