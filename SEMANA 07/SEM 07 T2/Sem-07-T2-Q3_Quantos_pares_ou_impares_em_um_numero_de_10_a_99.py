#Enunciado
'''
Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o
número lido.
• Nenhum dígito é ímpar.
• Apenas um dígito é ímpar.
• Os dois dígitos são ímpares.
'''
def eh_impar(numero):
	d = numero//10
	u = numero%10
	return (d, u)

def main():
	numero = int(input("Insira um número entre 10 e 99: ").strip())

	dezena, unidade = eh_impar(numero)
	if dezena % 2 == 1 and unidade % 2 == 1:
		print("Os dois dígitos são ímpares.")
	elif dezena % 2 == 1 or unidade % 2 == 1:
		print("Apenas um dígito é ímpar.")
	else:
		print("Nenhum dígito é ímpar.")

	

if __name__ == "__main__":
	main()