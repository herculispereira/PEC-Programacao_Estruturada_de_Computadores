'''
Escreva um programa que leia um caractere e mostra o 
valor booleano True (verdadeiro) se for um SÍMBOLO (o
que não é letra ou número) ou o 
valor booleano False (falso) caso contrário.
'''
caractere = input("Insira um caractere: ").lower().strip()

def vogal(caractere):
	return not caractere in "abcdefghijklmnopqrstuvwxyz0123456789"

print(vogal(caractere))