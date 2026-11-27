'''
Escreva um programa que leia uma lista com 10 números reais, 
calcule e mostre a lista, a quantidade de
números negativos e a soma dos números positivos dessa lista.
'''

def insercao():
	lista = []

	for i in range (10):
		numero = int(input("Insira o número: ").strip())

		lista.append(numero)

	return lista

def funcao_count_negativos(lista):

	contador_negativos = 0

	for i in lista:
		if i < 0:
			contador_negativos += 1

	return contador_negativos

def funcao_sum_positiva(lista):
	soma = 0 

	for i in lista:
		if i > 0:
			soma += i

	return soma

def main():
	lista = insercao()

	print(f"Lista {lista}")
	print(f"Quantidade de números negativos {funcao_count_negativos(lista)}")
	print(f"Soma de números positivos {funcao_sum_positiva(lista)}")

if __name__ == "__main__":
	main()