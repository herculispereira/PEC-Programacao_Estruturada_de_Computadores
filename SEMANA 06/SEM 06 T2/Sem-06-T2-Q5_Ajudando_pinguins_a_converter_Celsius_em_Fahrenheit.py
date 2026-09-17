#Enunciado
'''
Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? 
Vamos ajudá-los a converter temperaturas! Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. 
Lembre-se: Fahrenheit = (Celsius x (9 / 5)) + 32
'''

#Processamento
def celsius_para_fahrenheit(celsius):
	Fahrenheit  = ( celsius * (9/5))+32

	return Fahrenheit

def main():

    #Entrada
    celsius = float(input("Insira a temperatura em graus Celsius: ").strip())

	#Saída
    #Fahrenheit = celsius_para_fahrenheit(celsius)
    #print(f"{Fahrenheit:.2f}")
    print(f"{celsius} c° equivalem a {celsius_para_fahrenheit(celsius):.2f} °F")

if __name__ == "__main__":
	main()