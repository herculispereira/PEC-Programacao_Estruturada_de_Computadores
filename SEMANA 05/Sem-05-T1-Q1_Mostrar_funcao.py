#Enunciado
''' Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:

def calcular(a, b, c):
    return 2 * a + 5 * b - c
'''

#Entrada
numero1 = int(input("Insira um número: ").strip())
numero2 = int(input("Insira outro número: ").strip())
numero3 = int(input("Insira mais um número: ").strip())

#Criação de função com parametros
def calcular(a, b, c):
    return 2 * a + 5 * b - c

#chamando e saindo resultado da função
print("O Resultado da equação é ",calcular(numero1, numero2, numero3))