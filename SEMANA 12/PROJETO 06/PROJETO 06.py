from turtle import *

#Isso vai desenhar uma estrela cinza clara em um fundo azul escuro
bgcolor("MidnightBlue")

def drawPlanet(tamanho, cor):

    color(cor)
    pendown()
    begin_fill()

    for side in range (360):
        forward(tamanho)
        left(1)

def quadrado():
    pendown()
    begin_fill()

    for side in range (4):
        forward(40)
        left(90)

    end_fill()
    penup()


def drawStar(starSize, starColor):

    color(starColor)
    pendown()
    begin_fill()

    #desenha a forma da estrela
    for side in range(5):
        left(144)
        forward(starSize)

    end_fill()
    penup()

drawPlanet(5, "red")

hideturtle()
done()