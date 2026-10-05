#Enunciado
'''
Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, 
de acordo com os valores lidos:

• Todos os valores são diferentes;
• Existem dois valores iguais e um diferente;
• Todos os valores são iguais.
'''
def verificacao_de_igualdade(n1, n2, n3):
	if n1 == n2 == n3:
		return "Todos os valores são iguais"
	elif n1 != n2 and n1 != n3 and n2 != n3 and n3 != n1:
		return "Todos os valores são diferentes"

	else:
		return "Existem dois valores iguais e um diferente"

def main():

	numero1 = int(input("Insira o primeiro número: ").strip())
	numero2 = int(input("Insira o segundo número: ").strip())
	numero3 = int(input("Insira o terceiro número: ").strip())

	print(verificacao_de_igualdade(numero1, numero2, numero3))

if __name__ == "__main__":
	main()