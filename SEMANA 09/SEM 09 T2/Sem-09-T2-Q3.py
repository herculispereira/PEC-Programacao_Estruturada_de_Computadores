#Enunciado
'''
Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.
OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas;
Considere que em anos bissextos o mês de fevereiro tem 29 dias.

'''
def data_valida(data):

	dia = data[0:2]
	mes = data[2:4]
	ano = data[4:8]

	if int(ano) % 4 == 0 and int(ano) % 100 != 0 or ano % 400 == 0:
		
		if mes in "01030507081012":
				return 1 <= int(dia) <= 31

		elif mes in "04060911":
				return 1 <= int(dia) <= 30

		elif mes == "02":
				return 1 <= int(dia) <= 29
	else:
		if mes in "01030507081012":
				return 1 <= int(dia) <= 31

		elif mes in "04060911":
				return 1 <= int(dia) <= 30

		elif mes == "02":
				return 1 <= int(dia) <= 28

	return False

def main():

	data = input("Insira uma data no formato DDMMAAAA: ").strip()
		
	print(data_valida(data))

if __name__ == "__main__":
	main()