#Enunciado
'''
Desenvolva um programa que peça ao usuário o nível de volume atual e o nível de volume desejado de seu aparelho 
de som. Calcule e mostre a diferença de volume necessária. 
'''

# Entrada de dados
print('Iremos calcular a diferença de volume do seu som!\n')
v_atual = int(input('Insira o volume do som atual: ').strip())
v_desejado = int(input('Insira o volume que deseja: ').strip())

# Processamento
diferença = v_desejado - v_atual

# Saída de dados
print(f'A diferença é {diferença}')
