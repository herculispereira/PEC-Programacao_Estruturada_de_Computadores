'''
Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de
um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos
anteriores da lista original.
IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna
uma lista com a soma cumulativa.

Por exemplo:
minha_lista = [1, 2, 3, 4, 5]

somacumulativa(minhalista)

[1, 3, 6, 10, 15]
'''
def insercao():
	lista = []

	while True:
		
		numero = int(input(f"Insira o {len(lista)+1} número:").strip())
				
		if numero == 0:
			break
		
		lista.append(numero)		

	return lista

def soma_cumulativa(lista):

		somas = []
		quantidade = len(lista)	
		
		for numero in range(quantidade):
			soma = 0

			for contador in range(numero+1):
				soma += lista[contador]
			somas.append(soma) 

		return somas

def main():

	lista = insercao()
	print(f"Resultado: {soma_cumulativa(lista)}")

if __name__ == "__main__":
	main()