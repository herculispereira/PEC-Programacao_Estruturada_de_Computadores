#Enunciado
'''
Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador de letras. 
Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa frase sem considerar 
espaços em branco no início ou final da frase digitada.'''

#Processamento
def contagem_caractere(nome):
	contador = len(nome)

	return contador
def main():

	#Entrada
	frase = input("Insira uma frase: ").strip()


	#Saída
	print("A Frase possui",contagem_caractere(frase),"caracteres")

if __name__ == "__main__":
	main()