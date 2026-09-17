#Enunciado
'''
Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:

o maior número lido;
o menor número lido;
a média aritmética dos números lidos.
'''


#Processamento
def maior(x1, x2, x3, x4, x5):
	maior = max(x1, x2, x3, x4, x5)

	return maior

def menor(x1, x2, x3, x4, x5):
	menor = min(x1, x2, x3, x4, x5)

	return menor

def media(x1, x2, x3, x4, x5):

	media = (x1 + x2 + x3 + x4 + x5) / 5
	return media

def main():

	#Entrada
	n1 = int(input("Insira o Primeiro número: ").strip())
	n2 = int(input("Insira o Segundo número: ").strip())
	n3 = int(input("Insira o Terceiro número: ").strip())
	n4 = int(input("Insira o Quarto número: ").strip())
	n5 = int(input("Insira o Quinto número: ").strip())

	#Saída
	print("\nO Maior número digitado foi: ",maior(n1, n2, n3, n4, n5))
	print("O Menor número digitado foi: ",menor(n1, n2, n3, n4, n5))
	print("A Média dos números digitados é: ",media(n1, n2, n3, n4, n5))

if __name__ == "__main__":
	main()