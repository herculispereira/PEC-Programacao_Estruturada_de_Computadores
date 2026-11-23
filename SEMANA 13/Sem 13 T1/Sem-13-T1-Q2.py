'''
Escreva um programa que leia um número n. Considere uma lista com n posições, e então: 
a) preencha com 0 (zero) e imprima a lista; 
b) preencha com os números de 1 a n e imprima a lista; 
c) preencha com valores lidos pelo teclado e imprima a lista; 
d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista; 
dica: use insert para sempre incluir os elementos no início da lista;
'''
def insercao_nula(tamanho_lista):
		lista = []
		for i in range (tamanho_lista):
			lista.append(0)

		return lista

def insercao_nao_nula(tamanho_lista):
		lista = []
		for i in range (tamanho_lista):
			lista.append(i+1)

		return lista

def insercao_ordenada_teclado(tamanho_lista):
		lista = []
		for i in range (tamanho_lista):
			numero = int(input(f"Insira o {i+1} número: ").strip())
			lista.append(numero)

		return lista

def insercao_decrescente_teclado(tamanho_lista):
		lista = []
		for i in range (0, -tamanho_lista, -1):
			numero = int(input(f"Insira o {i+tamanho_lista} número: "))
			lista.insert(i, numero)

		return lista


def main():

	n = int(input("Insira o tamanho da lista: ").strip())
	
	print(f"Os Números inseridos foram {insercao_nula(n)}")
	print("\nProxima Lista!")
	print(f"Os Números inseridos foram {insercao_nao_nula(n)}")
	print("\nProxima Lista!")
	print(f"Os Números inseridos foram {insercao_ordenada_teclado(n)}")
	print("\nProxima Lista!")
	print(f"Os Números inseridos foram {insercao_decrescente_teclado(n)}")

if __name__ == "__main__":
	main()