#Enunciado
'''
Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido
que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.
'''

def verificacao(n1, n2, n3):

	if abs(n3 - n1) <= abs(n2 - n1):
		return abs(n3 - n1)
	else:
		return abs(n2 - n1)
	

def main():

	numero1 = int(input("Insira o primeiro número: ").strip())
	numero2 = int(input("Insira o Segundo número: ").strip())
	numero3 = int(input("Insira o Treceiro número: ").strip())

	print("A Menor diferença é",verificacao(numero1, numero2, numero3))

if __name__ == "__main__":
	main()