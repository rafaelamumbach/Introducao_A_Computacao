segundos = float (input("Digite um tempo em segundos: "))

segundos = segundos % (24 * 3600)
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(horas," horas e ", minutos, "minutos.")

## Desenvolva um programa em Python que solicite ao usuário digitar um tempo em segundos. Após a digitação, o computador
## deverá converter este tempo para horas e minutos e mostrar esta informação na tela do computador. Exemplo: para transformar a
## quantidade total de segundos em horas e minutos, deve-se utilizar os operadores de divisão que fornecem a parte inteira do
## quociente e o resto da divisão. Se o usuário digitar 15.987 segundos, o programa deverá mostrar na tela 4 horas e 26 minutos.