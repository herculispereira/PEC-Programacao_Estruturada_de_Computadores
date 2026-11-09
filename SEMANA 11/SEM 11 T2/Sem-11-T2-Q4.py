'''
O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
CÓDIGO PRODUTO PREÇO (R$)
H Hamburger 5.50
C Cheeseburger 6.80
M Misto Quente 4.50
A Americano 7.00
Q Queijo Prato 4.00
X PARA TOTAL DA CONTA

Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da
compra. Ao finalizar com “X”, exiba o total a pagar.
Observações:
• Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção
inválida.”.
• Enquanto o código não for 'X' o programa deve continuar lendo os itens.
Dica: Use upper() para ignorar a diferenças entre maiúscula e minúsculas; Use [0] para garantir que
apenas o primeiro caractere digitado seja considerado. Por exemplo:
codigo = input('Código: ').upper()[0]

'''


def cardapio_hamburgueria():

    total_da_conta = 0

    while True:


        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")

        opcao = input("Escolha uma opção: ").upper()[0]

        if opcao == "H":
            total_da_conta += 5.50

        elif opcao == "C":
            total_da_conta += 6.80

        elif opcao == "M":
            total_da_conta += 4.50

        elif opcao == "A":
            total_da_conta += 7.00

        elif opcao == "Q":
            total_da_conta += 4.00

        elif opcao == "X":
            break

        else:
            print("Opção inválida.")

    return total_da_conta


def main():

    print(f'O Valor total foi R$ {cardapio_hamburgueria():.2f}')


if __name__ == "__main__":
    main()
