'''
Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura
dos jogadores, determine:

a. o nome e a altura do jogador mais alto;
b. a média de altura do time;
c. os jogadores com altura superior à média, listando o nome e a altura de cada um.
'''
def insercao():
	lista_nome = []
	lista_altura = []

	for i in range(12):
		lista_nome.append(input(f"Insira o nome do {i+1} jogador: "))
		lista_altura.append(float(input(f"Insira a altura do {i+1} jogador: ")))

	return lista_nome, lista_altura

def maior_jogador(listaNomes, listaAlturas):
	nome_maior = ""
	altura_maior = 0

	for i in range(12):
		if listaAlturas[i] > altura_maior:
			nome_maior = listaNomes[i]
			altura_maior = listaAlturas[i]

	return nome_maior, altura_maior

def media_alturas(listaAlturas):
	soma_alturas = 0

	for i in range(12):
		soma_alturas += listaAlturas[i]

	return soma_alturas / 12

def maiores_que_media(listaNomes, listaAlturas, media):
	nomes_maiores = []
	alturas_maiores = []

	for i in range(12):
		if listaAlturas[i] > media:
			nomes_maiores.append(listaNomes[i])
			alturas_maiores.append(listaAlturas[i])		

	return nomes_maiores, alturas_maiores

def main():
	lista_nome, lista_altura = insercao()

	print("JOGADOR MAIS ALTO DO TIME")
	nome, altura = maior_jogador(lista_nome, lista_altura)
	print(nome)
	print(f"{altura:.2f}")

	print("ALTURA MÉDIA DO TIME")
	media = media_alturas(lista_altura)
	print(f"{media:.2f}")

	print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
	nomes_altos, alturas_altos = maiores_que_media(lista_nome, lista_altura, media)
	for i in range(len(nomes_altos)):
		print(nomes_altos[i])
		print(f"{alturas_altos[i]:.2f}")

if __name__ == "__main__":
	main()