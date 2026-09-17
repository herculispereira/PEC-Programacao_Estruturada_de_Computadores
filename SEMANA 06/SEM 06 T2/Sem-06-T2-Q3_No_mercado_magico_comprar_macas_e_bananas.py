#Enunciado
'''
Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total! 
Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.
'''

#Processamento
def total_em_frutas(precob, precom):
	total1 = precob * 2
	total2 = precom * 3

	return total1 + total2

def main():

	#Entrada
	preco_maca = float(input("Qual o preço da maça R$: ").strip())
	preco_banana = float(input("Qual o preço da banana R$: ").strip())

	#Saída
	print(f"O Preço total das frutas é R$ {total_em_frutas(preco_banana, preco_maca):.2f}")

if __name__ == "__main__":
	main()