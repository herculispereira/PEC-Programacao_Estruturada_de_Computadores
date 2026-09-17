#Enunciado
'''
Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h. 
Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia.
'''

#Entrada
print("Faremos Um Programa que mostre a quantidade de dias e sua viagem ira demorara !\n")
distancia = int(input(" Insira a Distancia do percuso: ").strip())
velocidade = int(input(" Insira a velocidade média em Km/h: ").strip())

#Processamento
#Calculo da quantidade total de horas
horas = distancia / velocidade

#Calculo da quantidade total de dias (obs: estamos pegando a somente parte inteira da divisão)
dias = int(horas / 24)

#Calculo da quantidade total de horas restantes (obs: estamos pegando a somente parte inteira do resto da divisão)
r_horas = int(horas % 24)

#Saida
print(f"{dias} dias e {r_horas} horas")
