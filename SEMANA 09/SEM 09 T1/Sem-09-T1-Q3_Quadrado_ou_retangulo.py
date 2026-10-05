#Enunciado
'''
Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. 
O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. 
Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, 
mostre o perímetro (soma de todos os lados) e a área (base vezes
a altura) do retângulo. Separe esses valores com um hífen.
'''

def verificacao(base, altura):

	if base == altura:
		return "QUADRADO"
	else:
		perimetro = base * 2 + altura * 2
		area = base * altura
		return f"{perimetro} - {area}"

def main():

	base = int(input("Base: ").strip())
	altura = int(input("altura: ").strip())

	print(verificacao(base, altura))

if __name__ == "__main__":
	main()