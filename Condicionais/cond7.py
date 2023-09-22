print("** CARDÁPIO **")
codigo_item = int(input("Informe o código do item -> "))
quantidade = int(input("Informe a quantidade de itens -> "))
preco = 0

if codigo_item == 100:
  preco = 10 * quantidade
  print("Item: Cachorro quente")
  print("Valor a ser pago: ", preco)

elif codigo_item == 101:
  preco = 18 * quantidade
  print("Item: Bauru simples")
  print("Valor a ser pago: ", preco)

elif codigo_item == 102:
  preco = 20 * quantidade
  print("Item: Bauru com ovo")
  print("Valor a ser pago: ", preco)

elif codigo_item == 103:
  preco = 5 * quantidade
  print("Item: Hamburguer")
  print("Valor a ser pago: ", preco)

elif codigo_item == 104:
  preco = 15 * quantidade
  print("Item: Cheese Burguer")
  print("Valor a ser pago: ", preco)

elif codigo_item == 105:
  preco = 4 * quantidade
  print("Item: Refrigerante")
  print("Valor a ser pago: ", preco)

else:
  print("ERRO: código do produto não reconhecido. Códigos válidos devem estar no intervalo de 100 a 105.")