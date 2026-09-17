#Enunciado
'''
Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. 
Mostre quantas fatias cada um recebe e quantas sobram.
'''


#Entrada
print("Faremos Um Programa que mostre quantas fatias cada pessoa ira ficar e quantas sobram!\n")
fatias = int(input("Digite a Quantidade de Fatias: ").strip())
pessoas = int(input("Digite a quantidade de pessoas: ").strip())

#Processamento
#Calculo de quantas fatia cada pessoa ira receber
#obs: o // é para garantir divisão onde o resultado é inteiro
recebimento = fatias // pessoas

#Quantidade de sobras ou seja o resto da divisão acima
sobras = fatias % pessoas 

#Saida
print(f"\nA Quantidade de fatias que cada pessoa vai receber será {recebimento} fatia(s)")
print(f"Sobraram {sobras} fatia(s)")
