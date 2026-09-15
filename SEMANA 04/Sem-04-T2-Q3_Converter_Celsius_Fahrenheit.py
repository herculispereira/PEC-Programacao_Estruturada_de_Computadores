#Enunciado
''' 
Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit:

Fahrenheit = (Celsius x (9 / 5)) + 3
'''

#Entrada
celsius = float(input("Insira a Temperatura em Graus Celsius: ").strip())


#Processamento
Fahrenheit  = ( celsius*(9/5))+32


#Saida
print("\nA Temperatura convertdida para Fahrenheit é ",Fahrenheit)