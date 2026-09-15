#Enunciado
''' 
Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. 
Considerar que a média é ponderada e que o peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é:

média ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
'''

#Entrada
n1 = float(input("Insira a Nota 01: ").strip())
n2 = float(input("Insira a Nota 02: ").strip())
n3 = float(input("Insira a Nota 03: ").strip())


#Processamento
media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10


#Saida
print("A Média ponderada dos números: ", media_ponderada)