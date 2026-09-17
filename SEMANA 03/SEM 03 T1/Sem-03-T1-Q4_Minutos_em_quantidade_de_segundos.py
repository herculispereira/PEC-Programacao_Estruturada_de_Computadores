#Enunciado
'''
O tempo é algo legal, especialmente quando você vai calcular quantos minutos há em um número 
específico de segundos. Peça ao usuário para inserir um número de segundos. Em seguida, 
use a divisão inteira para mostrar esse tempo em minutos (lembre-se, 1 minuto = 60 segundos) 
e use o resto da divisão inteira para saber quantos segundos sobram. Imprima os resultados.
'''

#Entrada
segundos = int(input("Insira a quantidade de minutos: ").strip())

#Processamento
#O // é para garantir divisão onde o resultado é inteiro
minutos = segundos // 60

#Quantidade de segundos que sobram é o resto da divisão acima
r_segundos = segundos % 60

#Saida
print(f"Em {segundos} seg. temos {minutos} minuto(s) e {r_segundos} seg. !")
