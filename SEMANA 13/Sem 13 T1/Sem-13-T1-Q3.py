'''
 Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro)
casas decimais.
b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa
decimal. Se n = 0, imprima “SEM NOTAS”.
c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes. 
Dica: certifique-se de ler apenas um caractere com input()[0] 
'''
def insercao_numeros(tamanho_lista):
	lista = []
   #lista[::-1]
	for i in range (tamanho_lista):
		item = float(input().strip())
		lista.append(item)

	return lista

def exibicao_oposta(tamanho_lista):
		lista = insercao_numeros(tamanho_lista)

		for i in range (tamanho_lista//2):
			aux = lista[i]
			lista[i] = lista[tamanho_lista-1-i]
			lista[tamanho_lista-1-i] = aux

		return lista

def notas_e_medias(tamanho_lista):

    if tamanho_lista == 0:
        return "SEM NOTAS", 0

    notas = insercao_numeros(tamanho_lista)
    soma_notas = 0

    for nota in notas:
        soma_notas += nota

    media = soma_notas / tamanho_lista

    return notas, media

def insercao_letras(tamanho_lista):
    consoantes = []
    qtd_vogais = 0

    vogais = "aeiouAEIOU"

    for i in range(tamanho_lista):
        item = input()[0]

        if item in vogais:
            qtd_vogais += 1
        else:
            consoantes.append(item)

    return qtd_vogais, consoantes

def main():

	n = int(input())

	print(exibicao_oposta(n))
	notas, media = notas_e_medias(n)
	print(notas)
	print(f"{media:.1f}")
	quantidade_vogais, letras = insercao_letras(n)
	print(quantidade_vogais)
	print(letras)


if __name__ == "__main__":
	main()