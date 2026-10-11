#Enunciado
'''
Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas,
dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores
e o ponto “.” no final da frase. Exemplos:

• 521 = cinco centenas, duas dezenas e uma unidade.
• 107 = uma centena e sete unidades.
• 80 = oito dezenas.

'''
def escrever_centena(centena):

	if centena == 1:
		return "uma centena"

	elif centena == 2:
		return "duas centenas"

	elif centena == 3:
		return "tres centenas"

	elif centena == 4:
		return "quatro centenas"

	elif centena == 5:
		return "cinco centenas"

	elif centena == 6:
		return "seis centenas"

	elif centena == 7:
		return "sete centenas"

	elif centena == 8:
		return "oito centenas"

	elif centena == 9:
		return "nove centenas"

def escrever_dezena(dezena):

	if dezena == 1:
		return "uma dezena"

	elif dezena == 2:
		return "duas dezenas"

	elif dezena == 3:
		return "tres dezenas"

	elif dezena == 4:
		return "quatro dezenas"

	elif dezena == 5:
		return "cinco dezenas"

	elif dezena == 6:
		return "seis dezenas"

	elif dezena == 7:
		return "sete dezenas"

	elif dezena == 8:
		return "oito dezenas"

	elif dezena == 9:
		return "nove dezenas"
	

def escrever_unidade(unidade):

	if unidade == 1:
		return "uma unidade"

	elif unidade == 2:
		return "duas unidades"

	elif unidade == 3:
		return "tres unidades"

	elif unidade == 4:
		return "quatro unidades"

	elif unidade == 5:
		return "cinco unidades"

	elif unidade == 6:
		return "seis unidades"

	elif unidade == 7:
		return "sete unidades"

	elif unidade == 8:
		return "oito unidades"

	elif unidade == 9:
		return "nove unidades"
	

def por_extenso(num):

	centena = num // 100
	dezena = num % 100 // 10
	unidade = num % 100 % 10

	if 1 <= num < 1000:

		if 1 <= centena <=9 and 1 <= dezena <=9 and 1 <= unidade <=9:
			return f"{escrever_centena(centena)}, {escrever_dezena(dezena)} e {escrever_unidade(unidade)}."

		elif 1 <= centena <=9 and dezena == 0 and 1 <= unidade <=9:
			return f"{escrever_centena(centena)} e {escrever_unidade(unidade)}."

		elif 1 <= centena <=9 and 1 <= dezena <= 9 and unidade == 0:
			return f"{escrever_centena(centena)} e {escrever_dezena(dezena)}."

		elif 1 <= centena <= 9 and dezena == 0 and unidade == 0:
			return f"{escrever_centena(centena)}."

		else:
			if 1 <= dezena <=9 and 1 <= unidade <=9:
				return f"{escrever_dezena(dezena)} e {escrever_unidade(unidade)}."

			elif 1 <= dezena <=9 and unidade == 0:
				return f"{escrever_dezena(dezena)}."

			else:
				return f"{escrever_unidade(unidade)}."

	else:
		raise ValueError(f"valor {num} inválido!")


def main():

	numero = int(input("Insira um número: ").strip())
		
	print(f"O número {numero} por extenso fica:\n{por_extenso(numero)}")

if __name__ == "__main__":
	main()