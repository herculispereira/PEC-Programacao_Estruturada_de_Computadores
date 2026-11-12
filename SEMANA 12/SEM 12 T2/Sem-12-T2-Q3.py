'''
Calcular H =1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o valor de H com 4 (quatro) casas decimais. O número n é lido
'''

def soma_fracoes(numero):
	soma = 1

	for n in range (2, numero+1):	
		soma += 1/n		 

	return soma

def main():

	numero = int(input("Insira um número: ").strip())

	print(f"{soma_fracoes(numero):.4f}")


if "__main__" == __name__:
	main()