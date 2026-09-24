#Enunciado
'''
Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou
“símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.
'''
def tipo_de_caractere(car):
	return car


def main():
	caractere = input("Digite um caractere: ").lower()

	if tipo_de_caractere(caractere) in "aeiou":
		print("vogal")

	elif tipo_de_caractere(caractere) in "bcdfghjklmnpqrstvwxyz":
		print(f"consoante")

	elif tipo_de_caractere(caractere) in "1234567890":
		print("número")
	else:
		print("símbolo")

if __name__ == "__main__":
	main()