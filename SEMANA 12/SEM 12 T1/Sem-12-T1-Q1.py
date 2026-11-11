'''
A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair n sua frente.
A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. Faça um programa que
leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance
a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.
'''

def alcanca(distancia_de_vantagem):
	velocidade_tartaruga = 1
	velocidade_lebre = 10

	distancia_tartaruga = distancia_de_vantagem
	distancia_lebre = 0

	while distancia_lebre < distancia_tartaruga:

		distancia_tartaruga += 1
		for j in range (velocidade_lebre):
			distancia_lebre += 1
			
		
	return distancia_lebre/velocidade_lebre



def main():

	distancia_de_vantagem = int(input("Insira a distancia de vantagem da tartaruga: ").strip())

	print(f"A Lebre alcançara a tartaruga em {alcanca(distancia_de_vantagem):.0f} minuto(s)")


if "__main__" == __name__:
	main()