'''
Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. 
Pedro também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. 
Considerando que a situação se refere ao mês de outubro do ano de 2016,

faça um programa leia o valor do salário e o valor da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, 
em que mês e ano a dívida com o cartão de crédito será superior ao seu próprio salário.

Represente os meses como inteiros de 1 a 12.

Dica: Controle essas quatro variáveis:

“dívida” que aumenta todo mês; “salário” que aumenta apenas se o número do mês for 3 (março); “mês” que é incrementado sempre, 
mas que retorna a 1 quando passar de 12; “ano” que só é incrementado quando o mês retornar a 1.

'''

def tempo_anos():

	mes = 10
	anos = 2016

	salario = float(input("Insira seu salário: ").strip())
	divida = float(input("Insira sua divida: ").strip())

	while divida < salario :

		divida += 0.15*divida

		if mes == 3:
			salario += 0.05*salario

		mes += 1
		if mes == 12:
			mes = 0
			anos += 1
		
	return f'sua divida ultrapassará o salário em {mes}/{anos}'

def main():

	print(tempo_anos())

if "__main__" == __name__:
	main()