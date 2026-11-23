'''
Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números
ímpares na lista IMPAR. Imprima as três listas.

'''
def insercao():
	lista = []

	for i in range (20):

		numero = int(input(f"Insira o {i+1} número:").strip())
		lista.append(numero)

	return lista

def eh_par(lista_numeros):
		lista_pares = []
		for i in lista_numeros:
			if i % 2 == 0:
				lista_pares.append(i)

		return lista_pares

def eh_impar(lista_numeros):
		lista_impares = []
		for i in lista_numeros:
			if i % 2 == 1:
				lista_impares.append(i)

		return lista_impares

def main():
	lista_numeros = insercao()

	print(f"A Lista dos números inseridos foram {lista_numeros}")
	print(f"Os números pares da lista são {eh_par(lista_numeros)}")
	print(f"Os números impares da lista são {eh_impar(lista_numeros)}")

if __name__ == "__main__":
	main()