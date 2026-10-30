'''
Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.
'''

def maior_numero():
    maior = 0

    for i in range (100):
        numero = int(input())
        if maior < numero:
            maior = numero

    return maior

def main():

    print(f'O Maior número inserido, foi {maior_numero()}')

if __name__ == "__main__":
    main()