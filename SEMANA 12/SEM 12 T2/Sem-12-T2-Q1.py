'''
Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
N ! = 1 x 2 x 3 x ... x N-1 x N
0 ! = 1
'''

def fatorial(numero):
	fatorial = 1

	if numero == 0:
		return 1

	while 1 < numero:
		fatorial *= numero 
		numero -= 1

	return fatorial

def main():

	numero = int(input("Insira um número: ").strip())

	print(f"{numero}! é igual a {fatorial(numero)}")


if "__main__" == __name__:
	main()