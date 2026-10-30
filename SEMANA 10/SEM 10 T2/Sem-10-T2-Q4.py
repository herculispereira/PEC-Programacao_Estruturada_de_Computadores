'''
Modifique mais um vez a canção dos programadores, dessa vez, gerando a canção dos bons
programadores, que resolvem 11 erros de cada vez e ao chegar a zero declaram que o software está
estabilizado. Atenção para o exemplo a seguir, especialmente, os versos finais.
99 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
88 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
77 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
...
11 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
Sem erros no software! Está estabilizado!
'''

def cancao():
    letra = ''
    for i in range (99, 0, -11):
        letra += str(i)+' bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"\n'

    return letra.strip()+"\nSem erros no software! Está estabilizado!"

def main():
    print(cancao())

if __name__ == "__main__":
    main()