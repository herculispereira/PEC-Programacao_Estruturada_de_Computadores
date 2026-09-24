#Enunciado
'''
Escreva um programa que leia três números correspondentes a três notas de um aluno. Apresente a média das três
notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média
final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.
'''
def media(nota1, nota2, nota3):
	media_aluno = (nota1 + nota2 + nota3) / 3
	return media_aluno


def main():
	n1 = float(input("Insira sua primeira nota: ").strip())
	n2 = float(input("Insira sua segunda nota: ").strip())
	n3 = float(input("Insira sua terceira nota: ").strip())

	media_final = media(n1, n2, n3)
	if n3 > 8:
		media_final += 1
		
		if media_final > 10:
			media_final = 10
			print(f"Sua média final é {media_final}")

		else:
			print(f"Sua média final é {media_final}")

	else:
		print(f"Sua média final é {media_final}")

if __name__ == "__main__":
	main()