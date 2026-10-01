#Enunciado
'''
Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas
obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios)/7

A atribuição dos conceitos obedece a tabela abaixo.

Conceito Média Final
A >= 9.0
B >= 7.5 e < 9.0
C >= 6.0 e < 7.5
D >= 4.0 e < 6.0
E < 4.0

O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado”
se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
'''

def media_final(n1, n2, n3, media_exercicios):	
	return (n1 + n2 * 2 + n3 * 3 + media_exercicios)/7

def main():
    matricula = input("Insira sua matricula: ").strip()
    nota1 = float(input("Insira sua primeira nota: ").strip())
    nota2 = float(input("Insira sua segunda nota: ").strip())
    nota3 = float(input("Insira sua terceira nota: ").strip())
    media_exercicios = float(input("Insira sua média dos exercicios:").strip())

    if media_final(nota1, nota2, nota3, media_exercicios) >= 9:
        print(matricula)
        print(f"{media_final(nota1, nota2, nota3, media_exercicios):.2f}")
        print("A")
        print("Aprovado")

    elif 7.5 <= media_final(nota1, nota2, nota3, media_exercicios) < 9:
        print(matricula)
        print(f"{media_final(nota1, nota2, nota3, media_exercicios):.2f}")
        print("B")
        print("Aprovado")

    elif 6 <= media_final(nota1, nota2, nota3, media_exercicios) < 7.5:
        print(matricula)
        print(f"{media_final(nota1, nota2, nota3, media_exercicios):.2f}")
        print("C")
        print("Aprovado")
    
    elif 4 <= media_final(nota1, nota2, nota3, media_exercicios) < 6:
        print(matricula)
        print(f"{media_final(nota1, nota2, nota3, media_exercicios):.2f}")
        print("D")
        print("Reprovado")

    else:
        print(matricula)
        print(f"{media_final(nota1, nota2, nota3, media_exercicios):.2f}")
        print("E")
        print("Reprovado")

if __name__ == "__main__":
	main()