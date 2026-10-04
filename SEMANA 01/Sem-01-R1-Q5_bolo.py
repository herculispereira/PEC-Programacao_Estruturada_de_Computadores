#Enunciado
'''
Crie um programa que mostre o algoritmo simplificado para fazer um bolo, em estilo de passos lógicos. 
Leia o ingrediente principal e mostre no resultado.
'''

# Entrada de dados
ingrediente_principal = input().strip().lower()

# Saída de dados
print(f'\nPara fazer um bolo de {ingrediente_principal.upper()} siga os passos: ')
print('1. Pegue os ingredientes: ovos, óleo, açucar, trigo e fermento.')
print(f'2. Junte tudo com {ingrediente_principal}.')
print('3. Ligar o forno a 180°C.')
print(f'4. No liquidificador, bater: ovos, óleo, açucar e {ingrediente_principal}.')
print('5. Em uma tigela, misturar conteúdo do liquidificador com farinha de trigo.')
print('6. Adicionar o fermento e misturar delicadamente,')
print('7. Untar a forma com manteiga e farinha.')
print('8. Despejar a massa na forma.')
print('9. Levar ao forno por aproximadamente 35 a 40 minutos.')
print('10. Assar até fazer o teste do palito e sair limpo.')
print('11. Retirar do forno e deixar esfriar.')
print(f'12. Servir o bolo de {ingrediente_principal.capitalize()}.')
