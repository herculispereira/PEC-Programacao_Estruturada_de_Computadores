#Enunciado
'''
Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva 
os que são maiores que a média. Considere duas casas decimais.
'''


def media(num1, num2, num3, num4, num5):
	media_numerica = (num1 + num2 + num3 + num4 + num5) / 5

	return media_numerica

def main():
	n1 = int(input().strip())
	n2 = int(input().strip())
	n3 = int(input().strip())
	n4 = int(input().strip())
	n5 = int(input().strip())

	print(f"{media(n1, n2, n3, n4, n5):.2f}")

	if media(n1, n2, n3, n4, n5) < n1:
		print(f"{n1:.2f}")
	
	if media(n1, n2, n3, n4, n5) < n2:
		print(f"{n2:.2f}")
	
	if media(n1, n2, n3, n4, n5) < n3:
		print(f"{n3:.2f}")
	
	if media(n1, n2, n3, n4, n5) < n4:
		print(f"{n4:.2f}")
	
	if media(n1, n2, n3, n4, n5) < n5:
		print(f"{n5:.2f}")


if __name__ == "__main__":
	main()