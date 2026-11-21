'''
Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.
'''
def soma(lista_numeros):
		soma = 0

		for i in lista_numeros:
			soma += i

		return soma

def multiplicacao(lista_numeros):
		total_multiplicacao = 1

		for i in lista_numeros:
			total_multiplicacao *= i

		return total_multiplicacao


def main():

	numeros = []

	for i in range (10):
		numero = int(input())
		numeros.append(numero)

	print(f"Os Números digitados foram: {numeros}")
	print(f"A Soma dos números digitados é {soma(numeros)}")
	print(f"A Multiplicação dos números digitados é {multiplicacao(numeros)}")


if __name__ == "__main__":
	main()