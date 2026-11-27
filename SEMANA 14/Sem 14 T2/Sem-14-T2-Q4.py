'''
Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o
produto escalar entre eles. Os conjuntos têm 5 elementos cada. 
Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: 
(x1 ∗ y1) + (x2 ∗ y2) + (x3 ∗ y3) + ⋯ + (xn ∗ yn).

Por exemplo, para as duas listas X e Y a seguir:

X = 2 5 7 3 9
Y = 3 8 1 0 4

O produto escalar será: (2 x 3) + (5 x 8) + (7 x 1) + (3 x 0) + (9 x 4) = 89
'''
def insercao():
	lista_A = []
	lista_B = []

	for i in range (5):
	
		numero = float(input("A - Insira o número: ").strip())
		lista_A.append(numero)

	for i in range (5):
	
		lista_B.append(float(input("B - Insira o número: ").strip()))

	return lista_A, lista_B

def produto_escalar(listaA, listaB):
	listaC = ""
	produto = 0

	for i in range (5):
		produto += listaA[i] * listaB[i]
		listaC += f"({listaA[i]:.0f} x {listaB[i]:.0f}) + "

	listaC = listaC.strip(" + ")

	listaC += f" = {produto:.0f}"

	return listaC

def main():
	lista_A, lista_B = insercao()

	print("Lista 1:",lista_A)
	print("Lista 2:",lista_B)

	print("Produto Escalar: ",produto_escalar(lista_A, lista_B))

if __name__ == "__main__":
	main()