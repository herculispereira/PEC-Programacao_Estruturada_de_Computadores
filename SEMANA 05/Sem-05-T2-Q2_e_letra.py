'''
Escreva um programa que leia um caractere e mostra o 
valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante)
 ou o valor booleano False (falso) caso contrário.
'''

caractere = input("Insira um caractere: ").lower().strip()

def vogal(caractere):
	return caractere in "abcdefghijklmnopqrstuvwxyz"

print(vogal(caractere))
 