#Enunciado
'''
Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.
'''

#Processamento
def contagem_caractere(nome):
	contador = len(nome)

	return contador
	
def main():

	#Entrada
	nome = input("Insira um nome: ").strip()


	#Saída
	print(f"No nome {nome} possui,",contagem_caractere(nome),"caracteres")

if __name__ == "__main__":
	main()