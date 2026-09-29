#Enunciado
'''
O índice de massa corporal (IMC) é uma medida internacional usada para calcular 
se uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo 
pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. 
Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula 
o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

IMC	Classificação
< 18,5	Abaixo do peso
< 25	Peso normal
< 30	Sobrepeso
< 35	Obeso leve
< 40	Obeso moderado
>=40	Obeso mórbido
'''
def calculo_imc(massa, altura):
	return massa / (altura * altura)


def categoria_imc(massa, altura):
	IMC = calculo_imc(massa, altura)

	if IMC < 18.5:
		return "Abaixo do peso"
	elif 18.5 <= IMC < 25:
		return "Peso normal"
	elif 25 <= IMC < 30:
		return "Sobrepeso"
	elif 30 <= IMC < 35:
		return "Obeso leve"
	elif 35 <= IMC < 40:
		return "Obeso moderado"
	else:
		return "Obeso mórbido"


def main():
	peso = float(input("Insira seu peso em Kg: ").strip())
	altura = float(input('Insira sua altura em m: ').strip())


	print(f"{calculo_imc(peso, altura):.2f}")
	print(categoria_imc(peso, altura))

if __name__ == "__main__":
	main()