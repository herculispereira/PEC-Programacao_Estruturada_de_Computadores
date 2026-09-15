''' Escreva um programa que leia dois valores e mostre na tela, nessa ordem:'''

#Entrada
x = float(input("Insira um número: ").strip())
y = int(input("Insira outro número: ").strip())


#Processamento
print("a. A soma dos números = ", x+y)
print("b. A concatenação das strings = ", str(x)+str(y))
print("c. A multiplicação dos números = ", x*y)
print("d. A multiplicação como strings = ", (str(x))*y)
print("e. A divisão dos números = ", x/y)
print("f. A divisão inteira dos números = ", x//y)
print("g. A exponenciação = ", x**y)
print("h. O módulo (resto) = ", x%y)
#Saida