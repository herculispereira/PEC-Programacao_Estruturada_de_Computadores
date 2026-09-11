#Enunciado
''' 
Escreva um programa que leia um preço e um valor percentual. Informe o preço com o aumento percentual e o 
preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e o valor percentual de 5 o programa 
deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.
'''

#Entrada
preco = float(input("Insira o Preço em R$: ").strip())
percentual = float(input("Insira o percentual de desconto ou acréscimo em %: ").strip())

#Criação de função
def aumento(preco, percentual):
    aumento = (1+percentual/100) * preco
    return aumento

def desconto(preco, percentual):
    desconto = (1-percentual/100) * preco
    return desconto

#chamando e saindo resultado da função
print (f"O Valor final com acescimo de {percentual:.2f} %% é %.2f" %aumento(preco, percentual) )
print (f"O valor final com desconto de {percentual:.2f} %% é %.2f" % desconto(preco, percentual))


  