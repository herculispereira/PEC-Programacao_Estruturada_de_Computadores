#Enunciado
'''
Escreva um programa que leia um único caractere pelo teclado e informe o código numérico
correspondente ao caractere lido.
'''

#Processamento
def codigo(letra):
	codigo_numerico = ord(letra)

	return codigo_numerico
	
def main():

	#Entrada
	caractere = input().strip()


	#Saída
	print(codigo(caractere))

if __name__ == "__main__":
	main()