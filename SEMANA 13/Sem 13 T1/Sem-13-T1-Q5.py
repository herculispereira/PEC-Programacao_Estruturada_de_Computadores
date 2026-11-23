'''
Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, 
cujos elementos sejam a intercalação dos elementos de A e B.

'''
def insecao_lista():
	lista = []	

	for i in range (25):
		numero = int(input().strip())
		lista.append(numero)

	return lista

def intercalador_listas(lista_A, lista_B):
		lista_C = []
		for i in range(25):
			lista_C.append(lista_A[i])
			lista_C.append(lista_B[i])

		return lista_C

def main():

	lista_A = insecao_lista()
	lista_B = insecao_lista()

	print(f"Lista A: {lista_A}")
	print(f"Lista B: {lista_B}")
	print(f"Lista Intercalada: {intercalador_listas(lista_A, lista_B)}")

if __name__ == "__main__":
	main()