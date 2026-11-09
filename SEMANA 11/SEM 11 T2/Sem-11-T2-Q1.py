'''
Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. 
Observação: A condição de saída do laço será a leitura do valor 0 (flag).

'''

def soma_numeros_inteiros():

	soma = 0

	while True:
		numero = int(input("Insira um número: ").strip())
		soma += numero

		if numero == 0:
			break

	return soma

def main():

	print(f'O Somatorio dos números digitados é {soma_numeros_inteiros()}')

if "__main__" == __name__:
	main()