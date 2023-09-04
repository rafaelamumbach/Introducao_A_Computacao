nota1 = float (input("Informe a primeira nota: "))
nota2 = float (input("Informe a segunda nota: "))
nota3 = float (input("Informe a terceira nota: "))

media_harmonica = 3 / (1/nota1 + 1/nota2 + 1/nota3)

print(f"Média harmônica: {media_harmonica:,.2f}")

## Desenvolva um programa em Python que solicite ao usuário informar três valores reais que correspondam a nota de um aluno, calcule
## e mostre na tela a média harmônica destas notas. A média harmônica de um conjunto de valores é um valor que tende ao menor dos valores
## sendo calculada pelo inverso da soma do inverso dos valores: Exemplo: se o usuário informar os valores 7.5, 6 e 9.5 respectivamente
## como a primeira, segunda e terceira notas de um aluno, o algoritmo deverá calcular a média 3/( 1/7.5 + 1/6 + 1/9.5) e mostrar o
## resultado final (7,39) na tela.