print("** OPERAÇÕES **")
print("✔ código = 1: multiplicar os três valores\n✔ código = 2: somar os três valores\n✔ código = 3: subtrair os três valores\n✔ código = 4: somar o cubo dos 3 valores")
codigo = int(input("Informe um código -> "))
a = int(input("Informe o valor a -> "))
b = int(input("Informe o valor b -> "))
c = int(input("Informe o valor c -> "))

if codigo == 1:
  mult = a * b * c
  print("Resultado: ", mult)

elif codigo == 2:
  somar = a + b + c
  print("Resultado: ", somar)

elif codigo == 3:
  subtracao = a - b - c
  print("Resultado: ", subtracao)

elif codigo == 4:
  cubo = (a * a * a) + (b * b * b) + (c * c * c)
  print("Resultado: ", cubo)

else:
  print("Código inválido.")