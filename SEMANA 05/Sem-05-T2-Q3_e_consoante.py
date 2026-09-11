'''
Escreva um programa que leia um caractere e mostra o 
valor booleano True (verdadeiro) se for uma CONSOANTE
ou o valor booleano False (falso) caso contrário
'''

caractere = input().lower("Insira um caractere: ").strip()

def vogal(caractere):
	return caractere in "bcdfghjklmnpqrstvwxyz"

print(vogal(caractere))