'''
Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e
parando em 250 ou antes.
99 bugs no software, pegue sete deles e conserte...
Tecle “Ctrl+F5”
106 bugs no software, pegue sete deles e conserte...
Tecle “Ctrl+F5”
113 bugs no software, pegue sete deles e conserte...
Tecle “Ctrl+F5”
...
Vamos fazer mais um café!
'''

def cancao():
    letra = ''
    for i in range (99, 251, 7):
        letra += str(i)+' bugs no software, pegue sete deles e conserte...\nTecle "Ctrl+F5"\n'

    return letra.strip()+"\nVamos fazer mais um café!"

def main():
    print(cancao())

if __name__ == "__main__":
    main()