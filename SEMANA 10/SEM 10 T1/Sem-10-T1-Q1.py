'''
Escreva um programa que mostre todos os números inteiros de 1 a 50 (um por linha).
'''
def contagem():
    numeros = ""
    for i in range (1, 51):
        numeros += str(i) + "\n"
    return numeros.strip()

def main():
    print(contagem())

if __name__ == "__main__":
    main()