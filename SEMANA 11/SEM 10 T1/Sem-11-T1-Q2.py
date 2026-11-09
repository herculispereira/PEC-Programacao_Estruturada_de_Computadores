'''
Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). 
Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero).

'''

def media_numeros_inteiros():
	contador = soma = 0

	while True:
		numero = int(input('Insira um número: ').strip())		

		if numero == 0:
			break

		soma += numero
		contador += 1

	return soma/contador

def main():

	print(f'A Média dos números digitados é {media_numeros_inteiros():.2f}')

if "__main__" == __name__:
	main()