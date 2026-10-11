#Enunciado
'''
Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"

Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''
def participacao_crime(p1, p2, p3, p4, p5):

	qtd_sim = (p1 == "S") + (p2 == "S") + (p3 == "S") + (p4 == "S") + (p5 == "S")

	if qtd_sim == 2:
		return "Suspeito"
	elif 3 <= qtd_sim <= 4:
		return "Cúmplice"
	elif qtd_sim == 5:
		return "Assassino"


	return "Inocente"

def main():
	print("Responda as perguntas a seguir com (S - N)")
	pergunta1 = input("Telefonou para a vítima? ").strip().upper()
	pergunta2 = input("Esteve no local do crime? ").strip().upper()
	pergunta3 = input("Mora perto da vítima? ").strip().upper()
	pergunta4 = input("Devia para a vítima? ").strip().upper()
	pergunta5 = input("Já trabalhou com a vítima? ").strip().upper()

		
	print(participacao_crime(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5))

if __name__ == "__main__":
	main()