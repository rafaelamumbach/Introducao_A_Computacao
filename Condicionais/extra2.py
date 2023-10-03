v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
v3 = int(input("Valor 3: "))
maior = 0
menor = 0

if (v1 > v2 and v1 > v3):
    maior = v1
    if (v2 < v3):
        menor = v2
    else:
        menor = v3

elif (v2 > v1 and v2 > v3):
    maior = v2
    if (v1 < v3):
        menor = v1
    else:
        menor = v3

else:
    maior = v3
    if (v1 < v2):
        menor = v1
    else:
        menor = v2

print("Maior:", maior)
print("Menor:", menor)