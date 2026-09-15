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
