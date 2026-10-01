#Enunciado
'''
Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para 'homens' e 2 para 'mulheres'. Usando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:

• para homens: (72.7 * altura) – 58

• para mulheres: (62.1 * altura) – 44.7.
'''

def altura_ideal_homem(alt):	
	return (72.7 * alt) - 58

def altura_ideal_mulher(alt):	
	return (62.1 * alt) - 44.7

def main():
	altura = float(input("Insira sua altura: ").strip())
	sexo = int(input("Qual o seu sexo?\n1 - Homem 2 - Mulher: ").strip())

	
	if sexo == 1:
		print(f"Seu peso ideal é {altura_ideal_homem(altura):.2f} Kg")
	elif sexo == 2:
		print(f"seu peso ideal é {altura_ideal_mulher(altura):.2f} Kg")
	else:
		print("Opção Invalida!")

if __name__ == "__main__":
	main()