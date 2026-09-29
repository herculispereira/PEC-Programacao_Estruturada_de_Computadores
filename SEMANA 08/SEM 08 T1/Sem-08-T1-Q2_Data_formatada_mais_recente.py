#Enunciado
'''
Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano)
 e escreva qual delas é a mais recente.
'''

def data_recente(d1, m1, a1, d2, m2, a2):
	
	if a1 < a2:
		return f"{d2}/{m2}/{a2}"
	else:
		if m1 < m2:
			return f"{d2}/{m2}/{a2}"
		else:
			if d1 < d2:
				return f"{d2}/{m2}/{a2}"
			else:
				return f"{d1}/{m1}/{a1}"


def main():

	print("Insira a primeira data!")
	dia1 = int(input("Insira o dia: ").strip())
	mes1 = int(input("Insira o mês: ").strip())
	ano1 = int(input("Insira o ano: ").strip())
	print("\nInsira a segunda data!")
	dia2 = int(input("Insira o dia: ").strip())
	mes2 = int(input("Insira o mês: ").strip())
	ano2 = int(input("Insira o ano: ").strip())

	print("\nA Data mais recente é",data_recente(dia1, mes1, ano1, dia2, mes2, ano2))


if __name__ == "__main__":
	main()