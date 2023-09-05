matricula =  int (input("Informe o número da matrícula do professor ==> "))
num_horas = float (input("Informe o número de horas-aula ministradas no mês  ==> "))
valor_hora = float (input("Informe o valor da hora-aula ==> "))
INSS = float (input("Informe a alíquota de recolhimento do INSS ==> "))

sal_bruto = valor_hora *num_horas

desc = sal_bruto * INSS / 100

sal_liquido = sal_bruto - desc

print(f"Matrícula: {matricula:,.2f} ",)
print(f"Salário Bruto: {sal_bruto:,.2f}")
print(f"Salário Líquido:{sal_liquido:,.2f} ")