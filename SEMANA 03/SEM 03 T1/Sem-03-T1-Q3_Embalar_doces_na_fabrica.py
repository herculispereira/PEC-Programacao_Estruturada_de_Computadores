#Enunciado
'''
A fábrica de doces precisa de ajuda para embalar os doces corretamente. 
Cada pacote deve conter um número inteiro de doces. 
Peça ao usuário para inserir o número de doces produzidos e o número de pacotes disponíveis. 
Divida os doces igualmente entre os pacotes fazendo a divisão inteira para garantir que cada 
pacote contém um número inteiro de doces. Imprima o número de doces em cada pacote

'''

#Entrada

doces = int(input("Quantidade de doces: ").strip())
pacote = int(input("Quantidade de pacote(s): ").strip())

#Processamento
t_pacote = doces // pacote 

#Saida
print(f"\nA Quantidade de pacote(s) é/são {t_pacote} pacote(s)")

