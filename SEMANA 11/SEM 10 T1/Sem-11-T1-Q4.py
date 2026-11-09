'''
Escreva um programa que leia número inteiro qualquer e mostre na forma invertida. Por exemplo:

Para o número lido	A saída será
123	        321
1895	    5981
14960	    6941
53698423	32489635

'''

def inverter_numeros(numero):

	invertido = ''

	if numero == 0:
		return f'{numero:.2f}'

	while numero > 0:
		
		invertido += str(numero%10)
		numero //= 10
		
	return int(invertido)

def main():

	numero = int(input("Insira um número inteiro: ").strip())

	print(f'\nO número {numero} invertido, fica {inverter_numeros(numero)}')

if "__main__" == __name__:
	main()