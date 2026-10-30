'''
Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade
de números pares e números ímpares contidos no mesmo.
'''

def e_par(n):
    return n % 2 == 0

def numeros_pares_e_impares ():  
    soma_par = 0
    soma_impar = 0  

    for i in range (100):

        numero = int(input(f'Insira o {i+1}° número: '))

        if e_par(numero):
            soma_par += 1
        else:
            soma_impar += 1

    return soma_par, soma_impar

def main():

    total_par, total_impar = numeros_pares_e_impares()
    print(f'\nO Total de pares inseridos é {total_par}\nO Total de ímpares inseridos é {total_impar}')

if __name__ == "__main__":
    main()