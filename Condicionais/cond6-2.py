codigo = int(input("Informe o código do seu cargo: "))
salario_antigo = float(input("Informe seu salário atual: "))
novo_salario = 0
valor_aumento = 0

if codigo == 101:
  novo_salario = salario_antigo * 0.10 + salario_antigo
  valor_aumento = novo_salario - salario_antigo
  print("Cargo: Gerente")
  print(f"Salário antigo: R${salario_antigo}")
  print(f"Novo salário: R${novo_salario}")
  print(f"Valor do aumento: R${valor_aumento}")

elif codigo == 102:
  novo_salario = salario_antigo * 0.20 + salario_antigo
  valor_aumento = novo_salario - salario_antigo
  print("Cargo: Engenheiro")
  print(f"Salário antigo: R${salario_antigo}")
  print(f"Novo salário: R${novo_salario}")
  print(f"Valor do aumento: R${valor_aumento}")

elif codigo == 103:
  novo_salario = salario_antigo * 0.30 + salario_antigo
  valor_aumento = novo_salario - salario_antigo
  print("Cargo: Técnico")
  print(f"Salário antigo: R${salario_antigo}")
  print(f"Novo salário: R${novo_salario}")
  print(f"Valor do aumento: R${valor_aumento}")

else:
  novo_salario = salario_antigo * 0.40 + salario_antigo
  valor_aumento = novo_salario - salario_antigo
  print("Cargo: Outros")
  print(f"Salário antigo: R${salario_antigo}")
  print(f"Novo salário: R${novo_salario}")
  print(f"Valor do aumento: R${valor_aumento}")