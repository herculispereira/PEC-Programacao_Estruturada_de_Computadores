#Entrada
n1 = float(input("Insira a Nota 01: ").strip())
n2 = float(input("Insira a Nota 02: ").strip())
n3 = float(input("Insira a Nota 03: ").strip())


#Processamento
media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10


#Saida
print("A Média ponderada dos números: ", media_ponderada)