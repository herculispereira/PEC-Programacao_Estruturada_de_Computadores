#Enunciado
'''
Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais!
 Sabendo que 1 ano terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.
'''

#Processamento
def anos_terrestre_para_anos_espaciais(idade):
	idade_espacial = idade // 2

	return idade_espacial

def main():

	#Entrada
	idade_terrestre = int(input("Insira sua idade terrestre: ").strip())


	#Saída
	print("Sua idade espacial é ",anos_terrestre_para_anos_espaciais(idade_terrestre))

if __name__ == "__main__":
	main()