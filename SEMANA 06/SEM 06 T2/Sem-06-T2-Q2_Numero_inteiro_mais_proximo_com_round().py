#Enunciado
'''
Nem sempre as transações financeiras resultam em números inteiros. 
Vamos usar o round() para resolver isso! Peça ao usuário para inserir uma quantidade de dinheiro. 
Em seguida, arredonde esse valor para o número inteiro mais próximo e imprima o resultado.
'''

#Processamento
def arredondar(valor):
	arredondado = round(valor, 0)

	return arredondado

def main():

	#Entrada
	dinheiro = float(input("Insira uma quantidade de dinheiro: ").strip())

	#Saída
	print(f"{arredondar(dinheiro):.0f}")

if __name__ == "__main__":
	main()