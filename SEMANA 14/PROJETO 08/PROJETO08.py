from random import *

def gerador_comprimentos():
	executa = True
	adjetivos = [ "maravilhoso", "acima da média", "excelente", "muito bom", "diferenciado" ]
	hobbies = [ "andar de bicicleta", "programar", "fazer chá", "praticar corrida", "cozinhar" ]

	print("Gerador de Cumprimentos")
	print("-----------------------")

	nome = input("Qual é o seu nome?: ")

	print('''
	Menu
	    c = obter cumprimento
	    a = adicionar hobby
	    d = remover hobby
	    p = imprimir hobbies
	    q = sair
	''')

	while executa == True:

	    menuChoice = input("\n>_").lower()

	    #'c' para um cumprimento
	    if menuChoice == 'c':

	        print("Aqui está o seu cumprimento", nome, ":")

	        #obtém um item aleatório de ambas as listas e
	        #adiciona-os ao cumprimento
	        print(nome, "você é", choice(adjetivos), "em",
	              choice(hobbies))
	        print("De nada!")

	    #'a' para adicionar hobby
	    elif menuChoice == 'a':

	        itemToAdd = input("Adicione o hobby: ")

	        if itemToAdd not in hobbies:
	        	hobbies.append(itemToAdd)

	        else:
	        	print("Item ja existente na lista")

	    #'d' para remover um hobby
	    elif menuChoice == 'd':

	        itemToDelete = input("Insira o hobby a ser removido: ")

	        if itemToDelete in hobbies:
	        	hobbies.remove(itemToDelete)

	        else:
	        	print("O Hobby não esta na lista!")

	    #'p' para imprimir a lista de hobbies
	    elif menuChoice == 'p':

	        print(hobbies)

	    #'q' para sair
	    elif menuChoice == 'q':

	        executa = False

	    else:

	        print("Insira uma opção válida!")

def gerador_nomes():

	executa = True

	nomes_machos = ["Rex", "Thor", "Bob", "Max", "Toby"]
	nomes_femeas = ["Luna", "Mel", "Nina", "Belinha", "Amora"]

	nomes_cachorros = ["Rex", "Toby", "Mel", "Bob", "Max"]
	nomes_gatos = ["Mimi", "Luna", "Nina", "Tom", "Felix"]


	print("SERVIÇO DE ESCOLHA DE NOMES PARA ANIMAIS")
	print("----------------------------------------")

	print('''MENU

		    s = sortear nomes
		    a = adicionar nome
		    d = remover nome
		    p = imprimir listas
		    q = sair
			''')


	while executa == True:

	    menuChoice = input("\nEscolha uma opção: ").lower()

	    # 's' para sortear nomes
	    if menuChoice == 's':

	        print('''Escolha o tipo de classificação:

					    1 = animais machos
					    2 = animais fêmeas
					    3 = cachorros
					    4 = gatos
					''')

	        categoria = int(input("Escolha uma categoria: "))

	        if categoria == 1:
	            lista = nomes_machos
	            descricao = "animais machos"

	        elif categoria == 2:
	            lista = nomes_femeas
	            descricao = "animais fêmeas"

	        elif categoria == 3:
	            lista = nomes_cachorros
	            descricao = "cachorros"

	        elif categoria == 4:
	            lista = nomes_gatos
	            descricao = "gatos"

	        else:
	            print("Categoria inválida!")
	            continue

	        quantidade = int(input("Quantos animais precisam de nomes?: "))

	        if quantidade <= 0:
	            print("Informe uma quantidade válida!")

	        elif len(lista) == 0:
	            print("Não existem nomes cadastrados nesta categoria!")

	        elif quantidade > len(lista):
	            print("Não existem nomes suficientes para todos os animais!")

	        else:
	            nomes_disponiveis = lista.copy()

	            print("\nSugestões de nomes para", descricao, ":")

	            for i in range(quantidade):

	                nome_sorteado = choice(nomes_disponiveis)

	                print(nome_sorteado)

	                nomes_disponiveis.remove(nome_sorteado)


	    # 'a' para adicionar nome
	    elif menuChoice == 'a':

	        print('''Escolha a lista:

					    1 = machos
					    2 = fêmeas
					    3 = cachorros
					    4 = gatos
					''')

	        categoria = int(input("Escolha uma categoria: "))

	        if categoria == 1:
	            lista = nomes_machos

	        elif categoria == 2:
	            lista = nomes_femeas

	        elif categoria == 3:
	            lista = nomes_cachorros

	        elif categoria == 4:
	            lista = nomes_gatos

	        else:
	            print("Categoria inválida!")
	            continue

	        itemToAdd = input("Digite o nome que deseja adicionar: ")

	        lista.append(itemToAdd)

	        print("Nome adicionado com sucesso!")


	    # 'd' para remover nome
	    elif menuChoice == 'd':

	        print('''Escolha a lista:

					    1 = machos
					    2 = fêmeas
					    3 = cachorros
					    4 = gatos
					''')

	        categoria = int(input("Escolha uma categoria: "))

	        if categoria == 1:
	            lista = nomes_machos

	        elif categoria == 2:
	            lista = nomes_femeas

	        elif categoria == 3:
	            lista = nomes_cachorros

	        elif categoria == 4:
	            lista = nomes_gatos

	        else:
	            print("Categoria inválida!")
	            continue

	        itemToDelete = input("Digite o nome que deseja remover: ")

	        if itemToDelete in lista:
	            lista.remove(itemToDelete)
	            print("Nome removido com sucesso!")
	        else:
	            print("Nome não encontrado!")


	    # 'p' para imprimir as listas
	    elif menuChoice == 'p':

	        print("\nNOMES PARA MACHOS:", nomes_machos)
	        print("NOMES PARA FÊMEAS:", nomes_femeas)
	        print("NOMES PARA CACHORROS:", nomes_cachorros)
	        print("NOMES PARA GATOS:", nomes_gatos)


	    # 'q' para sair
	    elif menuChoice == 'q':

	        executa = False

	        print("Obrigado por utilizar o programa,", nome)


	    else:

	        print("Insira uma opção válida!")



def main():
	opcao = int(input("Escolha\n1 - Gerador de mensagens\n2 - Gerador de nomes de animais\n>-"))

	if opcao == 1:
		gerador_comprimentos()

	elif opcao == 2:
		gerador_nomes()

	else:
		print("Opcão inválida!")

if __name__ == "__main__":
	main()
