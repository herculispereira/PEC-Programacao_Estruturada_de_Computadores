#Enunciado
'''
Escreva um programa que leia três números e mostre na tela em ordem crescente.
'''
def ordenar(n1, n2, n3):
	if (n1 < n2) and (n1 < n3) and (n3 < n2):
		aux = n2
		n2 = n3
		n3 = aux

	elif (n2 < n1) and (n2 < n3):
		aux = n1
		n1 = n2
		n2 = aux		
		if n3 < n2:
			aux = n2
			n2 = n3
			n3 = aux
	elif (n3 < n1) and (n3<n2):
		aux = n1
		n1 = n3
		n3 = aux
		if n3 < n2:
			aux = n2
			n2 = n3
			n3 = aux

			
	return (n1, n2, n3)

def main():

	numero1 = float(input("Insira o Primeiro número: ").strip())
	numero2 = float(input("Insira o Segundo número: ").strip())
	numero3 = float(input("Insira o Terceiro número: ").strip())

	numero1, numero2, numero3 = ordenar(numero1, numero2, numero3)

	print("Ordem Crescente",numero1, numero2, numero3)

if __name__ == "__main__":
	main()