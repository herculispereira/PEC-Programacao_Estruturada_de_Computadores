#Enunciado
'''
Um sacolão está vendendo frutas com a seguinte tabela de preços:

Item	Até 5Kg	Acima de 5Kg
Morango	R$ 2,50	R$ 2,20
Maça	R$ 1,80	R$ 1,50
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá 
ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de 
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

'''
def pagamento(morango, maca):

	if morango <= 5 and maca <= 5:

		if (morango + maca) > 8:
				return ((morango * 2.5) + (maca * 1.8)) * 0.9

		return (morango * 2.5) + (maca * 1.8)

	elif morango > 5 and maca > 5:

		if (morango + maca) > 8 or ((morango * 2.2) + (maca * 1.5)) > 25:
				return ((morango * 2.2) + (maca * 1.5)) * 0.9

		return (morango * 2.2) + (maca * 1.5)

	else:

		if maca > 5:

			if (morango + maca) > 8 or ((morango * 2.5) + (maca * 1.5)) > 25:
				return ((morango * 2.5) + (maca * 1.5)) * 0.9

			return (morango * 2.5) + (maca * 1.5)
		elif morango > 5:
			if (morango + maca) > 8 or ((morango * 2.2) + (maca * 1.8)) > 25:
				return ((morango * 2.2) + (maca * 1.8)) * 0.9

			return (morango * 2.2) + (maca * 1.8)

def main():

	morangos = float(input("Insira a quantidade de morangos em Kg: ").strip())
	macas = float(input("Insira a quantidade de maças em Kg: ").strip())

		
	print(f"O Preço total a ser pago será R$ {pagamento(morangos, macas):.2f}")

if __name__ == "__main__":
	main()