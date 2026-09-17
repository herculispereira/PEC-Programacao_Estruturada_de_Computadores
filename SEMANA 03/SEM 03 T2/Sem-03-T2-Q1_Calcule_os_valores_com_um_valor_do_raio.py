#Enunciado
'''
Escreva um programa que leia o valor de um raio, calcule e mostre na tela o 
comprimento da circunferência, a área do círculo, a área da esfera e o volume da esfera 
para o valor do raio lido. Mostre os valores com 6 casas decimais.
'''

# Entrada
raio = float(input("Insira o tamanho do raio: ").strip())

#Processamento
circunferencia = 2 * 3.141592 * raio
area_c = 3.141592 * raio ** 2
area_e = 4 * 3.141592 * raio **2
volume = 4/3 * 3.141592 * raio ** 3

#Saída
print(f'Circunferência: {circunferencia:.6f}')
print(f'Area do circulo: {area_c:.6f}')
print(f'Area da esfera: {area_e:.6f}')
print(f'Volume da esfera: {volume:.6f}')
