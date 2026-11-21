'''
Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura
de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista
onde cada valor da lista original é a multiplicado pelo valor da constante.
IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e
o valor da constante e retorna uma nova lista com os elementos multiplicados.
'''
def insercao():
	lista = []

	while True:

		numero = int(input("Insira um número: "))

		if numero == 0:
			break

		lista.append(numero)

	return lista


def multiplica_constante(lista_numeros, CONSTANTE):
		nova_lista_numeros = []

		for item in lista_numeros:
			nova_lista_numeros.append(item * CONSTANTE)

		return nova_lista_numeros

def main():

	
	lista = insercao()
	CONSTANTE = int(input("Insira a constante: "))
	print(multiplica_constante(lista, CONSTANTE))

if __name__ == "__main__":
	main()