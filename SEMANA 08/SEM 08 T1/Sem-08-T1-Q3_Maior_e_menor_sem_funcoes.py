#Enunciado
'''
Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. 
Considere que todos os valores são diferentes. NÃO use as funções min() e max().
'''

def menor(n1, n2, n3, n4, n5):
	if (n1 < n2) and (n1 < n3) and (n1 < n4) and (n1 < n5):
		return n1

	elif (n2 < n1) and (n2 < n3) and (n2 < n4) and (n2 < n5):
		return n2	

	elif (n3 < n1) and (n3 < n2) and (n3 < n4) and (n3 < n5):
		return n3

	elif (n4 < n1) and (n4 < n2) and (n4 < n3) and (n4 < n5):
		return n4

	else:			
		return n5

def maior(n1, n2, n3, n4, n5):
	if (n1 > n2) and (n1 > n3) and (n1 > n4) and (n1 > n5):
		return n1

	elif (n2 > n1) and (n2 > n3) and (n2 > n4) and (n2 > n5):
		return n2	

	elif (n3 > n1) and (n3 > n2) and (n3 > n4) and (n3 > n5):
		return n3

	elif (n4 > n1) and (n4 > n2) and (n4 > n3) and (n4 > n5):
		return n4

	else:			
		return n5

def main():

	numero1 = int(input("Insira o primeiro número: ").strip())
	numero2 = int(input("Insira o segundo número; ").strip())
	numero3 = int(input("Insira o terceiro número: ").strip())
	numero4 = int(input("Insira o quarto número: ").strip())
	numero5 = int(input("Insira o quinto número: ").strip())

	print("O maior numero inserido foi o",maior(numero1, numero2, numero3, numero4, numero5))
	print("O menor numero inserido foi o",menor(numero1, numero2, numero3, numero4, numero5))

	

if __name__ == "__main__":
	main()