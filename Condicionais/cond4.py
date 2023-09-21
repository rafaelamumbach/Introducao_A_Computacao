ano_nascimento = int(input("Ano de nascimento: "))
idade = 2023 - ano_nascimento
print("Idade: ", idade)

ano_sobra = 18 - idade
ano_atrasado = idade - 18

if idade == 18:
  print("* SITUAÇÃO *\nDeve se alistar ao serviço militar.")

elif idade < 18:
  print("* SITUAÇÃO *\nAinda é novo para o alistamento. Falta(m)", ano_sobra, "ano(s) para o alistamento obrigatório.")

elif idade > 18:
  print("* SITUAÇÃO *\nPassou do prazo de alistamento. Está", ano_atrasado,"ano(s) atrasado.")