'''
Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.
'''

def eh_primo(x, y):
	contador_de_divisores = 0
	numeros_primos = ""

	for n in range (x, y+1):

		for m in range (1, n+1):

			if n % m == 0:
				contador_de_divisores += 1

			if contador_de_divisores > 2:
				break

		if	contador_de_divisores == 2:
			numeros_primos += str(n) + "\n"

		contador_de_divisores = 0

	return numeros_primos.strip()

def main():
	print("Insira um intervalo de números e verificaremos se nele, possui numeros primos ou não!!\n")
	x = int(input("Número inferior do intervalo: ").strip())
	y = int(input("Número superior do intervalo: ").strip())

	print(f"Os Números primos no intervalo de {x} a {y} são:\n{eh_primo(x, y)}")


if "__main__" == __name__:
	main()