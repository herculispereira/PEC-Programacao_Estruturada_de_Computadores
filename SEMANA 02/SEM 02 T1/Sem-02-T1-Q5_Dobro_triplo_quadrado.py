#Enunciado
'''
Crie um programa em que o usuário insira um número inteiro X e você devolva o dobro, triplo e o quadrado de X. 
'''

#Contextualização do Programa
print("Iremos identificar o dobro, triplo e quadrado do seu número!\n")

# Entrada de dados
x = int(input("Digite um numero: ").strip())

# Processamento
dobro = x * 2
triplo = x * 3
quadrado = x * x

# Saída de dados
print(f"\nO Dobro de {x} é {dobro}")
print(f"O Triplo de {x} é {triplo}")
print(f"O Quadrado de {x} é {quadrado}")
