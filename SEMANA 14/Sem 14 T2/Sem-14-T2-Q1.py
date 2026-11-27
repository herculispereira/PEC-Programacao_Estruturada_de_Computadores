'''
Escreva um programa que leia 10 números inteiros e os armazene em uma lista. 
Imprima a lista, o maior elemento e a posição que ele se encontra.
'''

def insercao():
	lista = []

	for i in range (10):
		numero = int(input("Insira o número: ").strip())

		lista.append(numero)

	return lista

def funcao_max(lista):
	posicao = 0
	maximo = lista[0]
	tamanho_lista = len(lista)

	for i in range(tamanho_lista):
		if maximo < lista[i]:
			posicao = i
			maximo = lista[i]

	return maximo, posicao

def main():
	lista = insercao()
	print(f"Lista {lista}")
	
	maior, posicao = funcao_max(lista)
	print(maior)
	print(posicao)

if __name__ == "__main__":
	main()