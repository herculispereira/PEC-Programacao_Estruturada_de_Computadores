#Enunciado
'''
Você encontrou uma varinha mágica que pode dobrar qualquer coisa! Mas espere... Isso funcionaria com números? 
Vamos tentar! Peça ao usuário para inserir um número. Em seguida, calcule o dobro desse número e imprima o 
resultado.
'''

# Entrada de dados
print('Insira um número e mostrarei o seu dobro!\n')
numero = int(input('Digite um número: ').strip())

# Processamento
dobro = numero * 2

# Saída de dados
print(f'\nO Dobro de {numero} é {dobro}')
