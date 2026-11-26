'''
As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):

a) len(), que recebe uma lista e retorna número de itens;
b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
c) min(),que recebe uma lista e retorna o menor valor
d) max(), que recebe uma lista retorna o maior valor
e) sum(), que recebe uma lista retorna a soma dos valores
'''

def insercao():
	lista = []

	while True:
		numero = int(input("Insira o número: ").strip())

		if numero == 0:
			break

		lista.append(numero)

	return lista

def funcao_len(lista):

	contador = 0

	for i in lista:
		contador += 1

	return contador

def funcao_reverse(lista):

		tamanho_lista = funcao_len(lista)

		for i in range (tamanho_lista//2):
			aux = lista[i]
			lista[i] = lista[tamanho_lista-1-i]
			lista[tamanho_lista-1-i] = aux

		return lista

def funcao_min(lista):
	minima = lista[0]
	tamanho_lista = funcao_len(lista)

	for i in range(tamanho_lista):
		if minima > lista[i]:
			minima = lista[i]

	return minima

def funcao_max(lista):
	maximo = lista[0]
	tamanho_lista = funcao_len(lista)

	for i in range(tamanho_lista):
		if maximo < lista[i]:
			maximo = lista[i]

	return maximo

def funcao_sum(lista):
	soma = 0 
	tamanho_lista = funcao_len(lista)

	for i in range(tamanho_lista):
		soma += lista[i]
	return soma

def main():
	lista = insercao()
	print(f"Lista {lista}")
	print(f"Len {funcao_len(lista)}")

	print(f"Reverse {funcao_reverse(lista)}")

	print(f"Min {funcao_min(lista)}")
	print(f"Max {funcao_max(lista)}")
	print(f"Sum {funcao_sum(lista)}")

if __name__ == "__main__":
	main()