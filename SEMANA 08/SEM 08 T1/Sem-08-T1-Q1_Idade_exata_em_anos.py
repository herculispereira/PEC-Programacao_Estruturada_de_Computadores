#Enunciado
'''
Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, 
a data de nascimento de uma pessoa, calcule e escreva a idade exata em anos
'''

def idade_em_anos(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual):
	
	if dia_nascimento <= dia_atual and mes_nascimento <= mes_atual:
		idade = ano_atual - ano_nascimento
	else:
		idade = ano_atual - ano_nascimento- 1

	return idade


def main():
	dia = int(input("Insira o dia atual: ").strip())
	mes = int(input("Insira o mês atual: ").strip())
	ano = int(input("Insira o ano atual: ").strip())
	dia_nasc = int(input("Insira seu dia de nascimento: ").strip())
	mes_nasc = int(input("Insira seu mes de nascimento: ").strip())
	ano_nasc = int(input("Insira seu ano de nascimento: ").strip())

	print("Sua idade atual é de",idade_em_anos(dia_nasc, mes_nasc, ano_nasc, dia, mes, ano),"anos")


if __name__ == "__main__":
	main()