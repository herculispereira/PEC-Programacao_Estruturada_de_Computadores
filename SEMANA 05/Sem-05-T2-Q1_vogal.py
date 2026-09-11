'''
Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) 
se for uma vogal ou o valor booleano False (falso) caso contrário.
'''

caractere = input("Insira uma letra: ").lower().strip()

def vogal(caractere):
	return caractere in "aeiou"

print(vogal(caractere))
