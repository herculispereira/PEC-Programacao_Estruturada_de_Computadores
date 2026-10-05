#Enunciado
'''
Escreva um programa que leia dois valores e uma das seguintes operações, codificadas dessa forma, 
será executada:

1 – Adição

2 – Subtração

3 – Multiplicação

4 – Divisão

Calcule e escreva o resultado dessa operação sobre os dois valores lidos.
'''
def calcular(n1, n2, operador):

	if operador == 1:
		return n1 + n2
	elif operador == 2 :
		return n1 - n2
	elif operador == 3 :
		return n1 * n2

	else:
		return n1 / n2

def main():

	numero1 = int(input("Insira o primeiro número: ").strip())
	numero2 = int(input("Insira o segundo número: ").strip())
	operador = int(input("1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 – Divisão: ").strip())
	
	print(calcular(numero1, numero2, operador))

if __name__ == "__main__":
	main()