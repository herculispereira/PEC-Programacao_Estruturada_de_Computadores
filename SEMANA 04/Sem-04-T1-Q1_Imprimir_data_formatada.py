#Enunciado
''' 
Considere que as variáveis “dia”, “mês” e “ano” contém os valores respectivos de uma certa data. Escreva um comando “print” que imprima
 essa data no formato usado, por exemplo, “15/4/2020” ou “2/12/2004”.
'''

#Entrada
dia = int(input("Insira o Dia: ").strip())
mes = int(input("Insira o Mês: ").strip())
ano = int(input("Insira o Ano: ").strip())

#Saida
print(f"A Data Inserida foi {dia}/{mes}/{ano}")
