#01. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo:

#Definição da função bem_vindo
def bem_vindo():
		#Conteudo da função que sera exibido quando ela for chamada "Bem Vindo ao Python."
		print('Bem vindo ao python.')
#Definição da função mensagem passando o parametro (msg) como entrada
def mensagem(msg):
		#Imprimindo o conteudo pesente no parametro (msg) que agora é uma variavél local
		print(msg)
#Chamando a função bem_vindo e exibidno seu conteudo
bem_vindo()
#Chamndo a função mensagem e passando o parametro "Curso de Programação Estruturada"
mensagem("Curso de Programação Estruturada.")

'''
Descrição codigo: o código acima exibe duas mensagens, cada uma por meio de função
a 1 função chamada bem_vindo quando chamada retorna um texto
a 2 função chamada mensagem quando chamada e passando um parametro, ela exibe esse parametro
'''

#02. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo: 

#Definição da função eh_par passando o parametro (numero) como entrada
def eh_par(numero):
		# Retorno da função é um valor lógico resultada da comparação entre (numero % 2== 0)
		return numero % 2 == 0
#Chamando a eh_par() passando como entrada/parametro o numero 2 e exibindo o seu resultado 
#junto com o texto "2 é par?" dentro de um print
print('2 é par?', eh_par(2))
#Chamando a eh_par() passando como entrada/parametro o numero 3 e exibindo o seu resultado 
#junto com o texto "3 é par?" dentro de um print
print('3 é par?', eh_par(3))
#Chamando a eh_par() passando como entrada/parametro o numero 5 e exibindo o seu resultado 
# negado com o operador logico not junto com o texto "5 é par?" dentro de um print
print('5 é par?', not eh_par(5))

'''
Descrição codigo: o código acima exibido possui uma função chamada eh_par que recebe um parametro
quando chamada e passado o parametro ela retorna um valor boleano (True ou False) ao usuario em
relação ao numero ser par ou não
'''

#03. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo:

#Definição da função area_quadrada passando o parametro (lado) como entrada
def area_quadrada(lado):
	#Retorno da função que será o resultado da equação lado * lado
	return lado * lado
#Definição da função perimetro_quadrado passando o parametro (lado) como entrada
def perimetro_quadrado(lado):
	#Retorno da função que será o resultado da equação lado * 4
	return lado * 4
#Inserindo via teclado um valor real na variavel "valor_lado"
valor_lado = float(input('lado do quadrado: '))
#Chamando a função area_quadrada passando como parametro o valor da variavel "valor_lado" e exibindo 
#seu resultado junto com um texto concatenado
print('Área do quadrado:', area_quadrada(valor_lado))
#Chamando a função perimetro_quadrado passando como parametro o valor da variavel "valor_lado" e exibindo 
#seu resultado junto com um texto concatenado
print('Perímetro do quadrado:', perimetro_quadrado(valor_lado))

'''
Descrição codigo: o código acima exibido possui duas funções chamadas area_quadrada e perimetro_quadrado
quando chamada a area_quadrada e repassado como parametro um número inserido pelo usuario ela retorna o valor da area 
e é exibido ao usuario, enquanto a função perimetro_quadrado executa da mesma forma entretanto entregando o perimetro
'''

#04. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo:

#Definição da função percentual passando o parametro (lado e porcentagem) como entrada
def percentual(valor, porcentagem):
	#Retorno da função que será o resultado da equação valor x (porcentagem / 100)
	return valor * (porcentagem / 100)
#Inserindo via teclado um valor real na variavel "pr"
pr = float(input("Preço: "))
#Inserindo via teclado um valor real na variavel "vr_p"
vr_p = float(input("Percentual: "))
#Formula na qual a variavel "pr_acres" recebe o valor de "pr" acrescido do resultado da função percentual com os parametros (pr e vr_p)
pr_acres = pr + percentual(pr, vr_p)
#Formula na qual a variavel "pr_desc" recebe o valor de "pr" subtraido do resultado da função percentual com os parametros (pr e vr_p)
pr_desc = pr - percentual(pr, vr_p)
#Exibição das variaveis "pr, vr_p, pr_acres" concatenada com texto explicativo
print(f'R${pr} com acréscimo de {vr_p}% fica por R${pr_acres}')
#Exibição das variaveis "pr, vr_p, pr_desc" concatenada com texto explicativo
print(f'R${pr} com desconto de {vr_p}% fica por R${pr_desc}')

'''
Descrição codigo: o código acima exibido possui uma função chamada percentual que recebe dois parametros valor e percentual e atraves desses
parametros calculo o percentual sobre o valor. Nesse programa ela é utilizada para aplicar acrescimo a outra variavel
por meio de soma e desconto por meio de subtração, esses valores são exibidos ao usuario por meio de prints expicativos
'''

#05. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo: 

#Definição da função minutos_para_horas passando o parametro (qtd_minutos) como entrada
def minutos_para_horas(qtd_minutos):
	#A Variável "horas" local recebe a divisão inteira de "qtd_minutos" por 60
	horas = qtd_minutos	// 60
	#A Variável "minutos" local recebe o resto da divisão inteira de "qtd_minutos" por 60
	minutos = qtd_minutos	% 60
	#Retorno da função sendo um string contendo hora e minutos e textos concatenados
	return	f'{horas}h{minutos}min'
#Inserindo via teclado um valor inteiro na variavel "minutos" global
minutos	= int(input("Quantidade de minutos: "))
#A Variável "horas" global recebe o valor retornado pela função minutos_para horas, sendo repassado como parametro a varaiável "minutos" global
horas = minutos_para_horas(minutos)
#Exibição das variaveis "horas e minutos" globais concatenada com texto explicativo
print(f'{minutos} minutos são equivalentes a {horas}')

'''
Descrição codigo: o código acima exibido possui uma função chamada minutos_para_horas que recebe um parametro qtd_minutos
e atraves desse parametro tranforma ele em horas e minutos equivalentes e retorna em formato string. No caso acima ela é chamada 
passando como parametro um dado inserido para o usuario e seu retorno guardado em uma variavel "horas" e exibido em um print
'''

#06. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo: 

#Definição da função trocar passando o parametro (x1, x2) como entrada
def trocar(x1, x2):
		#Retorno da função, sendo os valores em sequancia opostos a forma como entraram na função
		return x2, x1
#Inserindo via teclado um valor inteiro na variavel "n1" global
n1 = int(input('Primeiro número: '))
#Inserindo via teclado um valor inteiro na variavel "n2" global
n2 = int(input('Segundo número: '))
#Chamando a função trocar passando como parametros (n1,n2) e retornando o resultado invertido e armazenando nas variaveis n1 e n2
n1, n2 = trocar(n1, n2)
#Exibição das variaveis "n1 e n2" globais concatenada com texto explicativo
print(f'Primeiro {n1}; Segundo {n2}')

'''
Descrição codigo: o código acima exibido possui uma função chamada trocar que recebe dois parametros x1 e x2 desses
parametros se retorna em ordem oposta. Nesse programa ela é utilizada para trocar dois valores digitados 
pelo usuario via teclado e exibido seus resultados ao final
'''

#07. Para o código abaixo, escreva uma linha de comentário fazendo a leitura do comando logo abaixo: 

#Definição da função inveter passando o parametro (numero) como entrada
def inveter(numero):
	# variavel "u" recebe o resto de numero % 10
	u = numero % 10
	print("4 Valor de u = ",u)
	#A Variável "numero" recebe o seu valor inteiro dividido por 10
	numero = numero // 10
	print("6 Valor de numero = ",numero)
	# variavel "d" recebe o resto de numero % 10
	d = numero % 10
	print("8 Valor de d = ",d)
	#A Variável "numero" recebe o seu valor inteiro dividido por 10
	numero = numero // 10
	print("10 Valor de numero = ",numero)
	# variavel "c" recebe o resto de numero % 10
	c = numero % 10
	print("12 Valor de c = ",c)
	#A Variável "numero" recebe o seu valor inteiro dividido por 10
	numero = numero // 10
	print("14 Valor de numero = ",numero)
	# variavel "m" recebe o resto de numero % 10
	m = numero % 10
	print("16 Valor de m = ",m)
	# A vriável "numero_invertido" recebe a soma total de 'u' por 1000, 'd' por 100, "c" por 10 e "m"
	numero_invertido = (u*1000)+ (d * 100) + (c * 10) + m
	#Retorno da função, sendo o valor presente na variavel "numero_invertido"
	return numero_invertido
#Inserindo via teclado um valor inteiro na variavel "n" global
n = int(input("Digite um número entre 1000 e 9999: "))
#Exibindo valores de "n" junto com a função trocar com passagem de parametro "n" e o resultado geral concatenado com textos
print(f'O inverso de {n} é {inveter(n)}')

'''
Descrição codigo: o código acima exibido possui uma função inveter que recebe um parametro numero e atraves desse
parametro realiza o calculo para transformar cada casa decimal desse número em um algarismo separado
e ao final retorna o seu valor invertido utilizando multiplicação inversa. No caso acima ela é chamada passando
como parametro um numero digitado pelo usuario e o seu resultado invertido é colocado/exibindo via print
'''


