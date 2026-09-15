#Enunciado
''' 
Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros 
para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde 
a ultima meia-noite até a hora lida
'''

#Entrada
hora = int(input("Insira a hora: ").strip())
minuto = int(input("Insira os minutos: ").strip())
segundo = int(input("Insira os segundos: ").strip())

#Processamento
s_hora = hora * 3600
s_minuto = minuto * 60
total_segundos = s_hora + s_minuto + segundo 

#Saida
print(f"\nO Total de segundos desde a ultima meia noite é {total_segundos} segundos")
