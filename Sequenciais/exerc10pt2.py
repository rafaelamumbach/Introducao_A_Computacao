matricula = int (input("Informe o número da matrícula do professor ==> "))
num_horas = float (input("Informe o número de horas-aula ministradas no mês  ==> "))
valor_hora = float (input("Informe o valor da hora-aula ==> "))
INSS = float (input("Informe a alíquota de recolhimento do INSS ==> "))
IR = float (input("Informe a alíquota de recolhimento do IR ==> "))

sal_bruto = valor_hora * num_horas
desc1 = sal_bruto * INSS / 100

desc2 = sal_bruto * IR / 100
sal_liquido = sal_bruto - desc1 -desc2

print(f"Matrícula: {matricula}")
print(f"Salário Bruto: {sal_bruto:,.2f}")
print(f"Total de Desconto: {desc1+desc2:,.2f}")
print(f"Salário Líquido: {sal_liquido:,.2f}")