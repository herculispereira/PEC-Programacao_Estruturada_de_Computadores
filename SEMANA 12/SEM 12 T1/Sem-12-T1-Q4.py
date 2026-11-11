'''
O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um
programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8
dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989
e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).
'''
def numero_da_sorte(data_nascimento):
    numero_sorte = 0
    digitos = 0

    while data_nascimento > 0:

        digitos = data_nascimento % 10
        numero_sorte += digitos
        data_nascimento //= 10        

    return numero_sorte

def main():

    data_nascimento = int(input("Insira sua data de nascimento: ").strip())

    print(f'O seu número da sorte é {numero_da_sorte(data_nascimento)}')

if __name__ == "__main__":
    main()