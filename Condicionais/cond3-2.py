altura = float(input("Informe a altura em metros => "))
sexo = input("Informe o sexo: (M) para masculino ou (F) para feminino => ")

if sexo == 'M' or sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com altura {altura} metros é {peso_ideal:.2f} kg.")

elif sexo == 'F' or sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com altura {altura} metros é {peso_ideal:.2f} kg.")
    
else:
    print("Código do sexo não reconhecido.")