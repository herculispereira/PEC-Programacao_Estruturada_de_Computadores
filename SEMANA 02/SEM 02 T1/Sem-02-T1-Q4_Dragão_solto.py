#Enunciado
'''
Um dragão come exatamente meia ovelha por dia. Pergunte ao usuário por quantos dias o dragão está solto. Calcule 
quantas ovelhas ele já comeu nesse tempo! 
'''

#Contextualização do Programa
print("Iremos calcular quantas ovelhas o dragão consome!\n")

# Entrada de dados
dias = float(input("Digite a quantidade de dias que o dragão esta solto: ").strip())

# Processamento
ovelhas = dias * 0.5

# Saída de dados
print(f"\nA Quantidades de ovelhas consumida é {ovelhas}")

