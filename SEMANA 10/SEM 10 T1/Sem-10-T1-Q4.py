'''
Escreva um programa que gere a seguinte sequência:

10, 20, 30, 40, ..., 990, 1000.
'''

def sequencia_numeros():
    numeros = ""

    for i in range (10, 1001, 10):
        numeros += str(i) +", "

    return numeros.strip(", ")+"."

def main():
    
        print(sequencia_numeros())

if __name__ == "__main__":
    main()