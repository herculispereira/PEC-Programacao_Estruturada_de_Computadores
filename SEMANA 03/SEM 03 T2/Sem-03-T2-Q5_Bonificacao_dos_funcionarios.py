#Enunciado
'''
A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa 
Escreva um programa que leia o tempo de serviço de um funcionário e o valor do bônus 
por ano trabalhado. Mostre na tela quanto será a bonificação do funcionário.
'''

# Entrada
anos = int(input("Insira O tempo de Trabalho: ").strip())
v_ano = float(input("Insira o valor recebido por ano de trabalho: ").strip())

#Processamento
bonus = anos*v_ano

#Saída
print(f'O seu bõnus por tempo de serviço será R$ {bonus:.2f} ')