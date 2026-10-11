#Enunciado
'''
Escreva um programa que leia um número e exiba o dia correspondente da semana. 
(1-domingo, 
2-segunda-feira,
3-terça-feira etc.), 
se digitar outro valor deve aparecer “valor inválido”

'''
def week_day(n):
	
	if n == 1:
		return "domingo"

	elif n == 2:
		return "segunda-feira"

	elif n == 3:
		return "terça-feira"

	elif n == 4:
		return "quarta-feira"

	elif n == 5:
		return "quinta-feira"

	elif n == 6:
		return "sexta-feira"

	elif n == 7:
		return "sábado"

	else:
		return "valor inválido"

def main():

	numero = int(input("Insira um número: ").strip())
		
	print(week_day(numero))

if __name__ == "__main__":
	main()