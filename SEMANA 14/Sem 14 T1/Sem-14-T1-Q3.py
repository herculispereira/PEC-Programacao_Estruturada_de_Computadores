'''
Dadas duas listas A e B contendo 20 elementos inteiros cada, 
gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.
'''
def insercao():
	lista = []

	for i in range(20):
		lista.append(int(input("Insira o número: ")))

	return lista

def soma(listaA, listaB):
	lista_soma = []

	for i in range(20):
		lista_soma.append(listaA[i] + listaB[i])

	return lista_soma

def main():
	lista_A = insercao()
	lista_B = insercao()
	lista_C = soma(lista_A, lista_B)
	
	print(f"Lista A: {lista_A}")
	print(f"Lista B: {lista_B}")
	print(f"Resultado: {lista_C}")


if __name__ == "__main__":
	main()