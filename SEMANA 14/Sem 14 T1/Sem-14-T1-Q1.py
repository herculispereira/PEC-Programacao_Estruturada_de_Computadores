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