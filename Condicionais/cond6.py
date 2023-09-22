preco_normal = float(input("Preço do produto: "))
print("Métodos de pagamento: ")
print("1- dinheiro ou cheque")
print("2- à vista no cartão de crédito")
print("3- duas vezes no cartão de crédito")
print("4- três ou mais vezes no cartão de crédito")

metodo = int(input("Código do método escolhido: "))

dinheiro = preco_normal - 0.10
cheque = preco_normal - 0.10
cartao = preco_normal - 0.05
duasvezes = preco_normal
tresvezes = preco_normal + 0.10
maisvezes = preco_normal + 0.10

if metodo == 1:
  print("Preço normal:", preco_normal)
  print("Preço final: ", dinheiro)

elif metodo == 2:
  print("Preço normal:", preco_normal)
  print("Preço final: ", cartao)

elif metodo == 3:
  print("Preço final:", preco_normal)

elif metodo == 4:
  print("Preço normal:", preco_normal)
  print("Preço final: ", tresvezes)

print("Fim da compra.")