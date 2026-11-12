'''
Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa
que leia um número e determine se ele é ou não primo.
'''

def eh_primo(numero):
	contador_de_divisores = 0

	for n in range (numero, 0, -1):
		if numero % n == 0:
			contador_de_divisores += 1	

	return contador_de_divisores == 2

def main():
	print("Insira um número e verificaremos se ele é primo ou não!!\n")
	numero = int(input("Insira um número: ").strip())

	print(f"{eh_primo(numero)}")


if "__main__" == __name__:
	main()