#Enunciado
'''
Um mago precisa misturar duas substâncias para criar uma poção. Peça ao usuário os dois volumes (em ml) e exiba 
o total da poção. 
'''

#Mensagem explicando o programa
print("Misturaremos duas substâncias para criarmos uma poção.\n")

# Entrada de dados
a = float(input("Digite o volume da primeira substancia em ml: ").strip())
b = float(input("Digite o volume da segunda substancia em ml: ").strip())

# Processamento
soma = a + b

# Saída de dados
print(f"\nO Volume de {a:.2f} com {b:.2f} é {soma:.2f}")
