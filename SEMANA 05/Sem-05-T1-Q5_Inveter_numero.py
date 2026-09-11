#Enunciado
''' 
Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. 
Por exemplo, se o número lido for 5678 deverá ser mostrado 8765.
'''

#Entrada
numero = int(input("Digite um número: ").strip())

#Processamento
def reverso(n):
    milhar = n // 1000
    centena = (n % 1000) // 100
    dezena = ((n % 1000) % 100) // 10
    unidade = ((n % 1000) % 100) % 10
    return unidade*1000+dezena*100+centena*10+milhar

#Saida
print("O Inverso de ",numero," é ",reverso(numero))



  