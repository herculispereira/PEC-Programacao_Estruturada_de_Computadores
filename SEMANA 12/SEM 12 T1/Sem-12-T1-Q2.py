'''
Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e
calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o
carro à vista.
'''
def comprar_carro(valor_carro):
    poupanca = 10000
    meses = 0

    while poupanca < valor_carro:
        poupanca *= 1.007
        valor_carro *= 1.004
        meses += 1
    return meses

def main():

    valor_carro = float(input("Insira o valor do carro R$: ").strip())
    print(f'Você conseguirá comprar o carro em {comprar_carro(valor_carro)} mes(es)')

if __name__ == "__main__":
    main()