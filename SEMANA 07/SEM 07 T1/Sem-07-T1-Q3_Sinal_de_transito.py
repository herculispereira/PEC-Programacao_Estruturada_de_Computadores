#Enunciado
'''
Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne
a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
'''
def sinal_de_transito(cor):
	return cor


def main():
	cor = input("Escolha uma opção:\n“V” - verde;\n“A” - amarelo;\n“E” - vermelho: ").strip().upper()
	
	if sinal_de_transito(cor) == "V":
		print("Siga")
	elif sinal_de_transito(cor) == "A":
		print("Atenção")
	else:
		print("Pare")

if __name__ == "__main__":
	main()