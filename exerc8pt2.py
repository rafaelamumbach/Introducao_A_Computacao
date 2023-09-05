nota1 = float(input("Informe a primeira nota: "))

nota2 = float(input("Informe a segunda nota: "))

nota3 = 3 * nota1 * nota2 / (nota1 * nota2 - nota2 - 2 *nota1)

print(f"O aluno precisa tirar na última avaliação a nota: {nota3:,.2f} ")

## Desenvolva um programa em Python que solicite ao usuário informar dois valores reais que correspondam a nota de um aluno, 
## calcule e mostre qual o valor mínimo da terceira nota para que este aluno seja aprovado considerando média harmônica 6.
## Exemplo: se o usuário informar os valores 7.5 e 6 respectivamente, o algoritmo deverá calcular o valor mínimo 
## ( 3 * 7,5 * 6/( 7,5 * 6 - 6 - 2 * 7,5) = 135/ (45-6-15) = 135/24 = 5,625) e mostrar o resultado final (5,625) na tela.