#Enunciado
'''
Escreva um programa que leia uma quantidade de minutos e 
mostre a quantidade de horas e minutos equivalente.
'''

# Entrada
minutos = int(input("Digite a quantidade de minutos: ").strip())
#v_ano = float(input().strip())

#Processamento
horas = minutos // 60
t_minutos = minutos % 60

#Saída
#print(f'{bonus:.2f}')
print(f'{minutos} min equivalem a {horas}h{t_minutos}min')
