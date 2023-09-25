i = int(input("Informe (i): "))
a = float(input("Informe (a): "))
b = float(input("Informe (b): "))
c = float(input("Informe (c): "))

maior = max(a, b, c)
menor = min(a, b, c)
intermediario = a + b + c - maior - menor

if i == 1:
    print(f"Valores: {menor}, {intermediario}, {maior}")

elif i == 2:
    print(f"Valores: {maior}, {intermediario}, {menor}")

elif i == 3:
    print(f"Valores: {menor}, {maior}, {intermediario}")

else:
    print("Valor de (i) inválido. Digite 1, 2 ou 3.")