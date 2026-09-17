#Enunciado
'''
Escreva um programa que leia dois valores, um dividendo e um divisor. 
Mostre o resultado da divisão e o resto da divisão inteira dos valores.
'''

# Entrada
dividendo = float(input("Insira o Valor do dividendo: ").strip())
divisor = float(input("Insira o valor do divisor: ").strip())


#Processamento
quociente = dividendo // divisor
resto = dividendo % divisor

#Saída
print(f'Quociente: {quociente:.4f}')
print(f'Resto: {resto:.4f}')
