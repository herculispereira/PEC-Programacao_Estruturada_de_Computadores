#Enunciado
'''
Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para
solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s)
nome(s) lido(s).
'''
def total_caracteres(nome1, nome2):
		return len(nome1+nome2)


def main():
	meu_nome = input("Insira seu nome: ").strip()
	estado_civil = int(input("Qual o seu estado Civil:\n1- Casado 2- Solteiro: ").strip())

	if estado_civil == 1:
		nome_conjuge = input("Insira o nome do seu cônjuge: ").strip()
		print(total_caracteres(meu_nome, nome_conjuge))

	else:
		print(total_caracteres(meu_nome, ""))

if __name__ == "__main__":
	main()