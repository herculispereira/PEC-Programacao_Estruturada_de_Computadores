'''
Escreva um programa que leia uma lista com 20 números inteiros. 
Escreva os elementos da lista eliminando elementos repetidos.
'''

def insercao():
	lista = []

	for i in range (20):

		lista.append(int(input(f"Insira o {i+1} número: ").strip()))

	return lista

def exclusao_repeticoes(lista):
	lista_final = []

	for i in lista:
		if i not in lista_final:
			lista_final.append(i)

	return lista_final

def main():
	lista = insercao()

	print(f"Lista Inserida: {lista}")
	print(f"Lista Final: {exclusao_repeticoes(lista)}")

if __name__ == "__main__":
	main()