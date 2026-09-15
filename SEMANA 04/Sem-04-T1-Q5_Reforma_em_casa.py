#Entrada
altura = int(input("Insira a altura: ").strip())
comprimento = int(input("Insira o comprimento: ").strip())
largura = int(input("Insira a largura: ").strip())

#Processamento
area_piso = largura * comprimento
volume_sala = altura * comprimento * largura
area_paredes = 2 * altura * largura + 2 * altura * comprimento 

#Saida
print(f"\nÁrea necessaria para piso será {area_piso} m²")
print(f"O Volume é {volume_sala} m³")
print(f"A Area das paredes são {area_paredes} m²")
