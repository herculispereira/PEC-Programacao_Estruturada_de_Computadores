#Enunciado
'''
Pergunte ao usuário quantos quilômetros até Marte e quantos quilômetros por hora sua nave espacial pode viajar. 
Calcule e mostre quanto tempo levaria para chegar a Marte. 
'''

# Entrada de dados
print('Calcularemos quanto tempo demora uma viagem até Marte!\n')
distancia = int(input('Insira a Distancia em Km (Quilometros): ').strip())
velocidade = int(input('Insira a velocidade em Km/h (quilometros por hora): ').strip())

#Processamento
tempo = distancia / velocidade


# Saída de dados 
print(f'\nO tempo em horas a uma velocidade de {velocidade}km/h para chegar em marte são {tempo} hora(s)')
