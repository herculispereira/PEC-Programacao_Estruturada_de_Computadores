'''
Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos
(com duas casas decimais).'''

def media_numeros(quantidade):
    soma_numeros = 0

    for i in range (quantidade):

        numero = float(input(f'Insira o {i+1}° número: '))
        soma_numeros += numero


    return soma_numeros / quantidade

def main():

    print(f'A Média dos números inseridos é {media_numeros(100):.2f}')

if __name__ == "__main__":
    main()