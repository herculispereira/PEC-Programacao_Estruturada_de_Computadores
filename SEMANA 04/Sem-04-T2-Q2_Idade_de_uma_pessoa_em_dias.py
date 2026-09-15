#Enunciado
''' 
Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. 
Considerar sempre os anos com 365 dias e os messes com 30 dias.
'''

#Entrada
anos = int(input("Anos: ").strip())
meses = int(input("Meses: ").strip())
dias= int(input("Dias: ").strip())



#Processamento
d_anos = anos * 365
d_meses = meses * 30
d_dias = d_anos + d_meses + dias


#Saida
print("Total de dias: ", d_dias)