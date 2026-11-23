'''
Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.
'''
def insercao():
	lista = []

	for i in range (100):

		numero = int(input(f"Insira o {i+1} número:").strip())
		lista.append(numero)

	return lista

def notas_maiores(lista_notas):
		maiores_6 = []	
		
		for indice in range(100):
			if lista_notas[indice] >=6:
				maiores_6.append(indice)
			
		return maiores_6

def main():

	lista = insercao()
	print(f"Resultado: {notas_maiores(lista)}")

if __name__ == "__main__":
	main()