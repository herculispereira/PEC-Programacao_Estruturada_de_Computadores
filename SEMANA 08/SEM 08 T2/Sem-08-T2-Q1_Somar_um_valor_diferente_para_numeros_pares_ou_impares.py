#Enunciado
'''
Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja
ímpar. Mostre na tela o resultado da operação.
'''

def eh_par(numero):	
	return numero % 2 == 0


def main():
	numero = int(input("Insira um número: ").strip())
	
	if eh_par(numero):
		numero += 5
		print("O número inserido é par, entao será adicionado 5 a ele e ira ficar",numero)
	else:
		numero += 8
		print("O número inserido é ímpar, entao será adicionado 8 a ele e ira ficar",numero)

	


if __name__ == "__main__":
	main()