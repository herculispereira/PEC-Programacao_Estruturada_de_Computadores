def calculadora_do_amor():

	print("<3 "*11)
	print("\t!!!Calculadora do amor!!!")
	print("<3 "*11)

	nome1= input("\nDigite o nome da primeira pessoa: ")
	nome2 = input("Digite o nome da Segunda pessoa: ")
	probabilidade_maxima = len(nome1+nome2)
	probabilidade = 0

	for i in range(len(nome1)):
		for j in range(len(nome2)):
			if nome1[i] == nome2[j]:
				probabilidade += 1


	percentual = (probabilidade / probabilidade_maxima)*100
	return f"\nA probabilidade de vocês darem certo, é de : {percentual:.2f}%"


def criptografar():
	#lista de letras para criptografar
	alfabeto = "hijbcdeaqr stxyuvwfgmnopklz,.!"
	palavra_criptografada = ""

	#a chave secreta é 3
	chave = int(input("Insira a chave criptografica: ").strip())

	mensagem = input("Por favor, entre com o texto para criptografar: ").strip()

	for letra in mensagem:

		if letra in mensagem:
			#encontre a posição da letra em alfabeto
			#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
			posicao = alfabeto.find(letra)

			#some a chave secreta para encontrar a posição da letra criptografada
			#% 26 significa 'volte para 0 quando você chegar no 26'
			novaPosicao = (posicao + chave) % 30

			#a letra criptografada está no alfabeto na nova posição
			letraCriptografada = alfabeto[novaPosicao]
			palavra_criptografada += letraCriptografada

		else:
			palavra_criptografada += letraCriptografada

	return f"Sua mensagem criptografada fica:  {palavra_criptografada}"

def descriptografar():
	#lista de letras para criptografar
	alfabeto = "hijbcdeaqr stxyuvwfgmnopklz,.!"
	palavra_descriptografado = ""

	#a chave secreta
	chave = int(input("Insira a chave criptografica: ").strip())

	mensagem = input("Por favor, entre com a mensagem para descriptografar: ").strip()

	for letra in mensagem:

		if letra in mensagem:
			#encontre a posição da letra em alfabeto
			#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
			posicao = alfabeto.find(letra)

			#some a chave secreta para encontrar a posição da letra criptografada
			#% 26 significa 'volte para 0 quando você chegar no 26'
			novaPosicao = (posicao - chave) % 30

			#a letra criptografada está no alfabeto na nova posição
			letraCriptografada = alfabeto[novaPosicao]
			palavra_descriptografado += letraCriptografada

		else:
			palavra_descriptografado += letraCriptografada

	return f"Sua mensagem criptografada fica: {palavra_descriptografado}"

def main():

	print("Bem Vindo! ")
	print("Escolha uma das opções abaixo:")
	opcao = int(input("1 - Calculadora do amor\n2 - Criptografar mensagem\n3 - Descriptografar mensagem\n"))

	if opcao == 1:
		print(calculadora_do_amor())
	elif opcao == 2:
		print(criptografar())
	elif opcao == 3:
		print(descriptografar())
	else:
		print("Obrigado pela Visita!")


if __name__ == "__main__":
	main()