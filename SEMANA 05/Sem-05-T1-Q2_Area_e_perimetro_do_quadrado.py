#Enunciado
''' Escreva um programa que ler o valor para um lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado.

'''

#Entrada
lado_quadrado = float(input("Insira o tamanho do lado do quadrado: ").strip())

#Criação de função
def perimetro(lado):
    return 4 * lado

def area(lado):
    return lado * lado

#chamando e saindo resultado da função
print ("A área do quadrado é %10.4f" % area(lado_quadrado))
print ("O perímetro do quadrado é %10.4f" % perimetro(lado_quadrado))
  