'''
Faça um programa que leia duas listas de 10 elementos. 
Crie uma lista que seja a união entre as 2 listas
anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.
'''

def insercao():
	lista_A = []
	lista_B = []

	for i in range (10):

		lista_A.append(int(input(f"A - Insira o {i+1} número: ").strip()))

	for i in range (10):

		lista_B.append(int(input(f"B - Insira o {i+1} número: ").strip()))

	return lista_A, lista_B

def juncao_listas(listaA, listaB):
	lista_aux = listaA + listaB
	listaC = []

	for i in lista_aux:
		if i not in listaC:
			listaC.append(i)

	return listaC

def main():
	lista_A, lista_B = insercao()

	print(f"Lista Concatenada: {juncao_listas(lista_A, lista_B)}")

if __name__ == "__main__":
	main()