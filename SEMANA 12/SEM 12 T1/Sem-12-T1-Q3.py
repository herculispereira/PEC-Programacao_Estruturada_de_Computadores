'''
Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3%
ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a
população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a
população do país A.
'''
def comparar_populacao(populacao_A, populacao_B):
    anos = 0

    while populacao_B < populacao_A:
        populacao_A *= 1.02
        populacao_B *= 1.03
        anos += 1
    return anos

def main():

    
    populacao_A = int(input("Insira a quantidade de individuos na primeira população: ").strip())
    populacao_B = int(input("Insira a quantidade de individuos na segunda população: ").strip())

    if populacao_A < populacao_B:
    	print(f'A População de {populacao_A} habiitantes, ultrapassrá a de {populacao_B} habitantes em {comparar_populacao(populacao_B, populacao_A)} ano(s)')

    else:
    	print(f'A População de {populacao_B} habiitantes, ultrapassrá a de {populacao_A} habitantes em {comparar_populacao(populacao_A, populacao_B)} ano(s)')

if __name__ == "__main__":
    main()