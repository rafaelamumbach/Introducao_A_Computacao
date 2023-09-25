print("-- BÔNUS DE NATAL --")
sexo = input("Informe seu sexo: ")
tempo = int(input("Informe seu tempo de trabalho em anos: "))
salario = float(input("Informe seu salário atual: "))
valor_bonus = 0

if sexo == 'M' or sexo == 'm' and tempo > 15:
  print("-- Bônus: 20% --")
  valor_bonus = salario * 0.20
  print(f"Valor do bônus: R${valor_bonus}")

elif sexo == 'F' or sexo == 'f' and tempo > 10:
  print("-- Bônus: 25% --")
  valor_bonus = salario * 0.25
  print(f"Valor do bônus: R${valor_bonus}")

else:
  print("-- Bônus: R$1.000,00 --")
  valor_bonus = salario + 1000
  print(f"Valor do bônus: R${valor_bonus}")