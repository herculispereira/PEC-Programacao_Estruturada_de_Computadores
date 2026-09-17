#Enunciado
'''
Escreva um programa de leia o preço de um produto e mostre na tela o valor 
com 10% de desconto arredondado para duas casas decimais.
'''

# Entrada
preco = float(input("Insrira o preço do produto R$: ").strip())

#Processamento
p_desconto = preco * 0.9

#Saída
print(f'O produto com desconto de 10% ficara R$ {p_desconto:.2f}')
