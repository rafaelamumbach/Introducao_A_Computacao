nota1 = float (input("Informe a primeira nota: "))
nota2 = float (input("Informe a segunda nota: "))
nota3 = float (input("Informe a terceira nota: "))

media_harmonica_pon = 6 / (1/nota1 + 2/nota2 + 3/nota3)

print(f"Média harmônica ponderada: {media_harmonica_pon:,.2f}")

## Desenvolva um programa em Python que solicite ao usuário informar três valores reais que correspondam a nota de um aluno,
## calcule e mostre na tela a média harmônica ponderada destas notas com peso 1 para a primeira nota, peso 2 para a segunda nota
## e peso 3 para a terceira nota. A média harmônica ponderada de um conjunto de valores é um valor que tende ao menor dos valores
## sendo calculada pelo inverso da soma do inverso dos valores considerando sua relevância (peso). Exemplo: se o usuário informar 
## os valores 7.5, 6 e 9.5 respectivamente como a primeira, segunda e terceira notas de um aluno, o algoritmo deverá calcular a
## média 6/( 1/7.5 + 2/6 + 3/9.5) e mostrar o resultado final (7,65) na tela.