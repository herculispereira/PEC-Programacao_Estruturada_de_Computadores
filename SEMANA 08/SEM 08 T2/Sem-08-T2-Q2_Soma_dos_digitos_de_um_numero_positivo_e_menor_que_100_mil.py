#Enunciado
'''
Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e
100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.
'''

def soma_digitos(numero):	
    um = numero // 10000
    m = numero % 10000 // 1000
    c = ((numero % 10000) % 1000) // 100
    d = (((numero % 10000) % 1000) % 100) // 10
    u = (((numero % 10000) % 1000) % 100) % 10
    return u+d+c+m+um

def main():
    numero = int(input("Digite um número: ").strip())

    if 0 < numero < 100000:
        print("A Soma dos digitos do número digitado é",soma_digitos(numero))

    else:
        print(-1)  


if __name__ == "__main__":
	main()