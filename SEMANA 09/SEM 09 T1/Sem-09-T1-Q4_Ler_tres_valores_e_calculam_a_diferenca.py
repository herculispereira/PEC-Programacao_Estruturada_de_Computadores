#Enunciado
'''
Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui
menor diferença com relação ao primeiro, imprimindo o valor da diferença.
'''

def verificacao(n1, n2, n3):

	if (n2 - n1) <= (n3 - n1):
		return n2 - n1
	else:
		return n3 - n1
	

def main():

	numero1 = int(input().strip())
	numero2 = int(input().strip())
	numero3 = int(input().strip())

	print(verificacao(numero1, numero2, numero3))

if __name__ == "__main__":
	main()