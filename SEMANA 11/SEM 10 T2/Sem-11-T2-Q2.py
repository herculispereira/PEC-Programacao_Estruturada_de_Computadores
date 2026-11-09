'''
Escreva um programa que, para um número indeterminado de pessoas:

leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada;
calcule e escreva o número de pessoas;
calcule e escreva a idade média do grupo;
calcule e escreva a menor idade e a maior idade.

'''

def avaliando_idades():
	
	contador_pessoas = soma_idades = menor_idade = maior_idade = 0

	while True:
		
		idade = int(input().strip())		

		if idade == 0:
			break

		if contador_pessoas == 0:
			menor_idade = maior_idade = idade		

		if menor_idade > idade:
			menor_idade = idade

		if maior_idade < idade:
			maior_idade = idade

		contador_pessoas += 1 
		soma_idades += idade

	return contador_pessoas, (soma_idades/contador_pessoas), menor_idade, maior_idade

def main():

	contador, media_idade, menor_idade, maior_idade = avaliando_idades()

	print(f'\nO Total de idades inseridas, foram: {contador}\nA Média das idades, foi: {media_idade:.2f}\nA Menor Idade foi: {menor_idade}\nA Maior Idade, foi: {maior_idade}')

	
if "__main__" == __name__:
	main()