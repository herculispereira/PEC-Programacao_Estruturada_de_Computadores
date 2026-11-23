'''
Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.
'''
def insercao():
	lista = []

	for i in range (100):

		numero = int(input(f"Insira o {i+1} número:").strip())
		lista.append(numero)

	return lista

def ordenacao(lista_numeros):		

		for item1 in range(100):
			for item2 in range (item1, 100):
				if lista_numeros[item1] > lista_numeros[item2]:
					aux = lista_numeros[item1]
					lista_numeros[item1] = lista_numeros[item2]
					lista_numeros[item2] = aux

		return lista_numeros

def multiplicacao(lista_numeros):	

		for indice in range(100):
				if indice % 2 == 0:
					lista_numeros[indice] *= 3

				else:
					lista_numeros[indice] *= 5

		return lista_numeros

def main():

	lista = insercao()
	lista_ordenada = ordenacao(lista)
	print(f"Resultado: {multiplicacao(lista_ordenada)}")

if __name__ == "__main__":
	main()