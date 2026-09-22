#Enunciado
'''
Você já se perguntou como seria um relógio que atrasa 3 minutos a cada hora? Vamos modelar isso com 
programação! Peça ao usuário para inserir o número de horas. Calcule e imprima o tempo que um relógio que atrasa 
3 minutos por hora estaria atrás. 
'''

# Entrada de dados
print('Direi quantas horas o relógio estara atrasado com base em 3 min por hora!\n')
horas = int(input('Digite a quantidade de horas: ').strip())

# Processamento
atraso = horas * 3

# Saída de dados
print(f'A quantidade de minutos em atraso é {atraso} minuto(s)')
