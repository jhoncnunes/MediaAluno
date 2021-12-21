'' Escrever um algoritmo que lê o número de identificação de um aluno,
 as 3 notas obtidas nas 3 verificações e a média dos exercícios (ME)
 que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:

 ma = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7

 A atribuição de conceitos obedece a tabela abaixo:

 Média de Aproveitamento    Conceito

 9,0                            A

 7,5 e < 9,0                    B

 6,0 e < 7,5                    C

 4,0 e < 6,0                    D

< 4,0                          E

 O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios,
 a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o
 conceito for A,B ou C e REPROVADO se o conceito for D ou E.'''

id_aluno = int(input("Digite ID do aluno: "))
nota1: float = float(input("Digite a Nota 1 : "))
nota2 = float(input("Digite a Nota 2 : "))
nota3 = float(input("Digite a Nota 3 : "))
me = ((nota1 + nota2 + nota3)/3)
print(me)
ma = (me + nota1 + (nota2 * 2) + (nota3 * 3)) / 7
print("O Aluno com o id:", id_aluno, "obteve as notas:")
print(f'{nota1:.2f}')
print(f'{nota2:.2f}')
print(f'{nota3:.2f}')
print(f"Sua Media de Aproveitamento é: {ma:.2f}")
if 9.0 <= ma <= 10.0:
    print("O aluno foi aprovado, com conceito A")
elif 9.0 > ma > 7.5:
    print("O aluno foi aprovado, com conceito B")
elif 6.0 > ma > 7.5:
    print("O aluno foi aprovado, com conceito  C")

if 4.0 <= ma <= 5.9:
    print("O aluno foi reprovado, com conceito D")

if ma <= 4.0:
    print("O aluno foi reprovado, com conceito E")
