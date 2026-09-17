#Enunciado
'''
Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. 
Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).
'''


#Processamento
def horas_minutos_segundos(seg):

	hora = seg // 3600
	minutos = (seg % 3600) // 60
	segundos = (seg % 3600) % 60

	return f"{hora}:{minutos}:{segundos}"

def main():

	#Entrada
	segundos = int(input("Insira o tempo em segundos: ").strip())
	
	#Saída
	print(f"{segundos} segundos equivalem a",horas_minutos_segundos(segundos))

if __name__ == "__main__":
	main()