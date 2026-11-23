'''
Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa
deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e
retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. Por exemplo:

esta_ordenado([1, 2, 2]) True

esta_ordenado(['b', 'a']) False

'''
def insercao(quantidade):
	lista = []

	for i in range (quantidade):

		try:
			valor = input(f"Insira o {len(lista)+1} valor: ").strip()
			lista.append(float(valor))

		except:
			lista.append(valor)

	return lista

def esta_ordenado(lista):
		quantidade = len(lista)
		
		for indice in range(quantidade-1):
			if lista[indice] > lista[indice + 1]:
				return "LISTA NÃO ORDENADA"
			
		return "LISTA ORDENADA"

def main():
	n = int(input("Insira a quantidade de itens, que deseja inserir: ").strip())
	lista = insercao(n)
	print(esta_ordenado(lista))

if __name__ == "__main__":
	main()