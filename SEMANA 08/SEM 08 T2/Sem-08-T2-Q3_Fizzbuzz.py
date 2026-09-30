#Enunciado
'''
Escreva um programa que leia um número inteiro positivo e escreva na tela:

• FIZZ se o número é divisível por três;
• BUZZ se o número é divisível por cinco;
• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
• O próprio número caso não seja divisível por três ou por cinco.
'''

def divisivel_por3(numero):	
	return numero % 3 == 0

def divisivel_por5(numero):	
	return numero % 5 == 0


def main():
	numero = int(input().strip())
	
	if divisivel_por3(numero) and divisivel_por5(numero):
		print("FIZZBUZZ")

	elif divisivel_por3(numero):
		print("FIZZ")			

	elif divisivel_por5(numero):
		print("BUZZ")

	else:
		print(numero)

	


if __name__ == "__main__":
	main()