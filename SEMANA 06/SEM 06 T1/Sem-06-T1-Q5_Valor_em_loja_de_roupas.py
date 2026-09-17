#Enunciado
'''
Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, 
vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. 
Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas 
casas decimais:

Valor para pagamento à vista, com desconto de 9%.
Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
Valor da prestação para pagamento em 10 vezes, com 17% de juros.
'''

#Processamento
def ah_vista(preco, taxa_de_desconto):
	novo_preco = preco * (1 - taxa_de_desconto / 100)

	return novo_preco

def dividido_5x(preco):
	prestacao = preco / 5

	return prestacao

def dividido_10x(preco, taxa_de_juros):
	novo_preco = preco * (1 + taxa_de_juros / 100)
	prestacao = novo_preco / 10
	return prestacao

#Saída
def main():

	#Entrada
	preco = float(input("Insira o preço do produto R$: ").strip())
	TAXA_DESCONTO = 9
	TAXA_JUROS = 17

	a_vista = ah_vista(preco, TAXA_DESCONTO)
	prestacao_5x = dividido_5x(preco)
	prestacao_10x = dividido_10x(preco, TAXA_JUROS)
	print(f"\nCom Desconto de {TAXA_DESCONTO}% fica por R$ {a_vista:.2f}")
	print(f"Dividido em 5x fica R$ {prestacao_5x:.2f} o valor da prestação.")
	print(f"Dividido em 10x fica R$ {prestacao_10x:.2f} o valor da prestação.")

if __name__ == "__main__":
	main()