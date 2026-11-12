'''
A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
sempre será maior ou igual a 2.
'''

def fibonacci(numero):
	acumulador = ""
	atual = 0
	proximo = 1

	for i in range (numero):	

		acumulador += str(atual)  + ", "	

		novo_numero = atual + proximo
		atual = proximo
		proximo = novo_numero
		 

	return acumulador.strip(", ")

def main():

	numero = int(input("Insira a quantidade de termos que deseja: ").strip())

	print(f"{fibonacci(numero)}")


if "__main__" == __name__:
	main()