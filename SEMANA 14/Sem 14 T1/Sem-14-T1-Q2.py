'''
Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe
uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo
count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2
aparece na lista.
Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois
o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.
'''
def insercao():
	lista = []

	while True:
		numero = int(input("Insira um número: ").strip())

		if numero == 0:
			break

		lista.append(numero)

	return lista

def funcao_count(lista, numero):

	contador = 0

	for i in lista:
		if numero == i:
			contador += 1

	return contador

def main():
	
	lista = insercao()
	numero = int(input().strip())
	
	print(lista)
	print(numero)
	cont = funcao_count(lista, numero)
	print(cont)


if __name__ == "__main__":
	main()