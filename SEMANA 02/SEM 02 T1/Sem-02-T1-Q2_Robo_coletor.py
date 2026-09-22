#Enunciado
'''
Um robô coleta 12 peças por hora. Quantas peças ele terá coletado após certo número de horas?  
'''

print("Iremos verificar quantas coletas um robô consegue fazer em horas!\n")

# Entrada de dados
horas = float(input("Digite a quantidade de horas trbalhada pelo robô: ").strip())

# Processamento
total = horas * 12

# Saída de dados
print(f"\nO Total de coletas em {horas} hora(s) será {total} coletas")
