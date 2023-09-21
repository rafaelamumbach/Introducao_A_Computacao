print("** EMPRÉSTIMO **")
valor_casa = float(input("Valor da casa -> "))
salario = float(input("Salário -> "))
anos = int(input("Anos: "))

prestacao_mensal = valor_casa / (anos * 12)
limite_salario = salario * 0.3

if prestacao_mensal >= limite_salario:
  print("Empréstimo negado.")

else:
  print("Empréstimo aceito.")