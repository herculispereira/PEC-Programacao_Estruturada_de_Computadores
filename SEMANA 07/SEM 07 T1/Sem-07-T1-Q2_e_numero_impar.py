#Enunciado
'''
Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou
o valor booleano False (falso) caso contrário.
'''
def impar_ou_par(num):
	return num % 2


def main():
	numero = int(input("Insira um número: ").strip())
	
	if impar_ou_par(numero) == 1:
		print(True)

	else:
		print(False)

if __name__ == "__main__":
	main()