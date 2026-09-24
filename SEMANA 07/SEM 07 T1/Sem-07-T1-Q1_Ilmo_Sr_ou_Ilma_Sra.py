#Enunciado
'''
Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo
Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro
1 para identificar masculino e 2 para identificar feminino.
'''
def sr_ou_sra(genero):
	return genero


def main():
	nome = input("Insira seu nome: ").strip()
	sexo = int(input("Insira seu Genero\n1- Masculino 2- Feminino: ").strip())

	if sr_ou_sra(sexo) == 1:
		print(f"Ilmo Sr. {nome}")

	else:
		print(f"Ilma Sra. {nome}")

if __name__ == "__main__":
	main()