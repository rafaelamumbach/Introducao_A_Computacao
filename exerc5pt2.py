nota1 = float (input("Informe a primeira nota: "))
nota2 = float (input("Informe a segunda nota: "))
nota3 = float (input("Informe a terceira nota: "))

media_ponderada = (2.5 * nota1 + 2.5 * nota2 + 5 * nota3) / 10

print("Média ponderada: ", media_ponderada)

## Desenvolva um programa em Python que solicite ao usuário informar três valores reais que correspondam
## a nota de um aluno, calcule e mostre na tela a média ponderada com peso 2,5 para a primeira e segunda notas
## e peso 5 para a terceira nota. A média ponderada de um conjunto de valores é calculada multiplicando os pesos
## pelos respectivos valores, somando estes valores e dividindo pela soma dos pesos: Exemplo: se o usuário informa
## os valores 7.5, 6 e 9.5 respectivamente como a primeira, segunda e terceira notas de um aluno, o algoritmo deverá
## calcular a média ( 2.5*7.5 + 2.5*6 + 5* 9.5)/10 e mostrar o resultado final (8,12) na tela.