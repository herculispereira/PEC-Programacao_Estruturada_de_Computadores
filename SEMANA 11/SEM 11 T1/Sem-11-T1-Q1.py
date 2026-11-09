'''
Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. 
Mostre em quantos anos o valor acumulado será o dobro do valor inicial. Por exemplo:

R$100,00 rendendo 8% ao ano irá dobrar em 10 anos.
Tempo	Valor
Início	R$ 100.00
1 ano	R$ 108.00
2 anos	R$ 116.64
3 anos	R$ 125.97
4 anos	R$ 136.05
5 anos	R$ 146.93
6 anos	R$ 158.69
7 anos	R$ 171.38
8 anos	R$ 185.09
9 anos	R$ 199.90
10 anos	R$ 215.89
R$100,00 rendendo 10% ao ano irá dobrar em 8 anos.
Tempo	Valor
Início	R$ 100.00
1 ano	R$ 110.00
2 ano	R$ 121.00
3 anos	R$ 133.10
4 anos	R$ 146.41
5 anos	R$ 161.05
6 anos	R$ 177.16
7 anos	R$ 194.87
8 anos	R$ 214.36
R$100,00 rendendo 15% ao ano irá dobrar em 5 anos.
Tempo	Valor
Início	R$ 100.00
1 ano	R$ 115.00
2 anos	R$ 132.25
3 anos	R$ 152.09
4 anos	R$ 174.90
5 anos	R$ 201.14

'''

def total_com_juros(valor_inicial, taxa_juros):
	total = valor_inicial
	tempo = 0

	while total < (valor_inicial * 2):
		total += taxa_juros/100*total
		tempo += 1

	return tempo



def main():

	deposito_inicial = float(input('Insira o valor inicial de depósito: ').strip())
	taxa_de_juros = float(input('Insira a Taxa de Juros: ').strip())

	print(f"Em {total_com_juros(deposito_inicial, taxa_de_juros)} ano(s) o valor de R$ {deposito_inicial:.2f} dobrará")


if "__main__" == __name__:
	main()