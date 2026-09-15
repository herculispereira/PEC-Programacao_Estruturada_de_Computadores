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