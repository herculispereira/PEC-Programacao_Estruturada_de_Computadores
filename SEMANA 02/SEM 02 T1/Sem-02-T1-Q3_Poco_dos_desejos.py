#Enunciado
'''
Você encontrou um poço dos desejos, mas ele só realiza desejos que envolvem matemática! Peça ao usuário para 
inserir o valor encontrado no poço. Agora calcule quantas moedas de R$0,25 somam o valor no poço sem 
ultrapassar o total encontrado. 
'''

#Contextualização do Programa
print("Iremos verificar quantas moedas de R$ 0,25 voce possui!\n")

# Entrada de dados
x = float(input("Digite a quantidade de dinheiro em Reais (R$) que encontrou no poço: ").strip())

# Processamento
#Iremos pegar somente a parte inteira da divisão, pois a saida será sempre em um nico digito
total = int(x / 0.25)

# Saída de dados
print(f"O Total de moedas de R$ 0,25 são {total} moeda(s).")
