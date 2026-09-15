#Enunciado
''' 
Escreva um programa que leia três números inteiros nas variáveis “a”, “b” e “c” e escreva a média deles:

(a + b + c) / 3
'''

#Entrada
a = int(input("Insira um número: ").strip())
b = int(input("Insira Outro número: ").strip())
c = int(input("Insira mais um número: ").strip())

#Processamento
media = (a+b+c)/3

#Saida
print(f"\nA Média dos números digitadoes é {media}")
