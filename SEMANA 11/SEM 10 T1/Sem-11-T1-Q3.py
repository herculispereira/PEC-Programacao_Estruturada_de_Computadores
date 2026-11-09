'''
Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). 
Ao final, o programa deve mostrar o maior e o menor de todos os números lidos (excluindo o zero).

'''

def maior_e_menor():

	maior = menor = 0

	while True:

		numero = int(input('Insira um número: ').strip())

		if numero == 0:
			break

		if maior == 0 and menor == 0:
			maior = menor = numero

		if maior < numero:
			maior = numero

		if menor > numero:
			menor = numero		
		
	return maior, menor

def main():

	maior, menor = maior_e_menor()
	print(f'O Maior número inserido, foi: {maior}\nO Menor número inserido, foi: {menor}')

if "__main__" == __name__:
	main()