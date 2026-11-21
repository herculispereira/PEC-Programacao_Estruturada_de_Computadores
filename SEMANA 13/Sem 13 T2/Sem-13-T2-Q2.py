'''
Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.
'''
def insercao():
	lista = []

	for i in range (4):

		numero = int(input(f"Insira um número: "))
		lista.append(numero)

	return lista


def ordenacao(lista_numeros):
		

		for item1 in range(4):
			for item2 in range (item1, 4):
				if lista_numeros[item1] > lista_numeros[item2]:
					aux = lista_numeros[item1]
					lista_numeros[item1] = lista_numeros[item2]
					lista_numeros[item2] = aux


		return lista_numeros

def multiplicacao(lista_numeros):
		nova_lista_numeros = lista_numeros		

		for indice in range(4):
				if indice % 2 == 0:
					lista_numeros[indice] *= 3

				else:
					lista_numeros[indice] *= 5


		return nova_lista_numeros, lista_numeros

def main():

	lista = insercao()
	print(ordenacao(lista))
	print(multiplicacao(lista))

if __name__ == "__main__":
	main()