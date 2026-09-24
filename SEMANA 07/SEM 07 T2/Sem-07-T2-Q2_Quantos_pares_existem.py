#Enunciado
'''
Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse
número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.
'''
def eh_par(numero):
	c = numero//100
	d = numero%100//10
	u = numero%100%10
	return (c, d, u)


def main():
	numero = int(input().strip())
	contador_par = 0
	centena, dezena, unidade = eh_par(numero)

	if 100 <= numero <=999:
		if centena % 2 == 0 and dezena % 2 == 0 and unidade % 2 == 0:
			contador_par += 3

		elif (centena % 2 == 0 and dezena % 2 == 0) or (centena % 2 == 0 and unidade % 2 == 0) or (dezena % 2 == 0 and unidade % 2 == 0):
			contador_par +=2

		else:
			contador_par +=1

		
	else:
		if dezena % 2 == 0 and unidade % 2 == 0:
			contador_par +=2
		elif dezena % 2 == 0 or unidade % 2 == 0:
			contador_par += 1
		else:
			contador_par = 0

	print(contador_par)

if __name__ == "__main__":
	main()