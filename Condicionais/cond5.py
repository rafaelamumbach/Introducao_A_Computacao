nascimento = int(input("Informe seu ano de nascimento: "))
idade = 2023 - nascimento

if idade <= 9:
  print("Idade:", idade, "\nMirim.")

elif idade <= 14 and idade > 9:
  print("Idade:", idade, "\nInfantil.")

elif idade <= 19 and idade > 14:
  print("Idade:", idade, "\nJunior.")

elif idade <= 20 and idade > 19:
  print("Idade:", idade, "\nSênior")

elif idade > 20:
  print("Idade:", idade, "\nMaster.")