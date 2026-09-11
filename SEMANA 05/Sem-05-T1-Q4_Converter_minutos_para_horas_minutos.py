#Enunciado
''' 
Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertidade para 
horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos
'''

#Entrada
tempo_em_minutos = int(input("Insira o tempo em minutos: ").strip())

#Criação de função
def horas(minutos):
    total_horas = minutos // 60
    return total_horas

def minutos(minutos):
    totas_minutos= minutos % 60
    return totas_minutos

#chamando e saindo resultado da função
print (f"O Equivalente a {tempo_em_minutos} minuto(s), são %.f"%horas(tempo_em_minutos)+":%.f min"%minutos(tempo_em_minutos))


  