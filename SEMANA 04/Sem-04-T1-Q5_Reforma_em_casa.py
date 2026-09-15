#Enunciado
''' 
Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser usada nas paredes. 
Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. 
Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima:

Área do piso da sala: largura * comprimento

Volume da sala: largura * comprimento * altura

Área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento
'''

#Entrada
altura = int(input("Insira a altura: ").strip())
comprimento = int(input("Insira o comprimento: ").strip())
largura = int(input("Insira a largura: ").strip())

#Processamento
area_piso = largura * comprimento
volume_sala = altura * comprimento * largura
area_paredes = 2 * altura * largura + 2 * altura * comprimento 

#Saida
print(f"\nÁrea necessaria para piso será {area_piso} m²")
print(f"O Volume é {volume_sala} m³")
print(f"A Area das paredes são {area_paredes} m²")
