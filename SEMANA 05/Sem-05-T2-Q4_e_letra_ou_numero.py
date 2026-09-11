'''
Escreva um programa que leia um caractere e 
mostra o valor booleano True (verdadeiro) 
se for uma LETRA (vogal
ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou 
valor booleano False (falso) caso contrário
'''

caractere = input("Insira um caractere: ").lower().strip()

def vogal(caractere):
	return caractere in "abcdefghijklmnopqrstuvwxyz0123456789"

print(vogal(caractere))