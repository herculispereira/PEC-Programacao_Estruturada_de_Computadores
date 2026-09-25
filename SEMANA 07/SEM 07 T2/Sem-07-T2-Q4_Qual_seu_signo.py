#Enunciado
'''
04. Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. 
Considere exatamente:
Áries (21/03 a 19/04); 
Touro (20/04 a 20/05); 
Gêmeos (21/05 a 21/06); 
Câncer (22/06 a 22/07); 
Leão (23/07 a 22/08); 
Virgem (23/08 a 22/09); 
Libra (23/09 a 22/10); 
Escorpião (23/10 a 21/11); 
Sagitário (22/11 a 21/12);
Capricórnio (22/12 a 19/01); 
Aquário (20/01 a 18/02); 
Peixes (19/02 a 20/03);
'''

def signo(dia, mes):
	  
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        meu_signo = "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        meu_signo = "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        meu_signo = "Gêmeos"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
        meu_signo = "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        meu_signo = "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        meu_signo = "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        meu_signo = "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        meu_signo = "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        meu_signo = "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        meu_signo = "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        meu_signo = "Aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    	meu_signo = "Peixes"
    else:
    	meu_signo = "Data Inválida!"

    return meu_signo

def main():

	dia = int(input("Insira o seu dia de nascimento: "))
	mes = int(input("Insira seu mês de nascimento: "))

	print(signo(dia, mes))

if __name__ == "__main__":
	main()
