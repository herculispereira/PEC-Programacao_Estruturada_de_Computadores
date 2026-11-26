'''
Foram anotados nomes, idades e alturas de 30 alunos. 
Faça um programa que determine quais
alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a
altura arredondando para duas casas decimais.
'''
def insercao():
	lista_nome = []
	lista_idade = []
	lista_altura = []

	for i in range(30):
		lista_nome.append(input(f"insira o {i+1} nome: ").strip())
		lista_idade.append(int(input(f"insira a {i+1} idade: ").strip()))
		lista_altura.append(float(input(f"insira a {i+1} altura: ").strip()))

	return lista_nome, lista_idade, lista_altura

def media_alturas(listaAlturas):
	soma_alturas = 0

	for i in range(30):
		soma_alturas += listaAlturas[i]

	return round(soma_alturas / 30, 2)

def menores_que_media(listaNomes, listaIdades, listaAlturas, media):
	nomes_menores = []

	for i in range(30):
		if listaAlturas[i] < media and listaIdades[i] > 13:
			nomes_menores.append(listaNomes[i])	

	return nomes_menores

def main():
	lista_nome, lista_idade, lista_altura = insercao()
	media = media_alturas(lista_altura)

	print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
	nomes_baixos = menores_que_media(lista_nome, lista_idade, lista_altura, media)

	for i in range(len(nomes_baixos)):
		print(nomes_baixos[i])	

if __name__ == "__main__":
	main()