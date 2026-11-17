
from turtle import *
from random import *

def moveToRandomLocalization():
    penup()
    setpos(randint(-400, 400), randint(-280, 280))
    pendown()


def drawStar(starSize, starColor):

    color(starColor)
    pendown()
    begin_fill()

    # Desenha a forma da estrela
    for side in range(5):
        left(144)
        forward(starSize)

    end_fill()
    penup()


def drawGalaxy(numberOfStars):

    starColours = ["white", "blue", "green", "gray"]

    moveToRandomLocalization()

    for star in range(numberOfStars):

        penup()
        left(randint(-180, 180))
        forward(randint(5, 20))
        pendown()

        drawStar(9, choice(starColours))


def drawConstellation(numberOfStars):

    moveToRandomLocalization()

    for star in range(numberOfStars - 1):

        drawStar(randint(7, 15), "white")

        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))

    drawStar(randint(7, 15), "white")


def drawPlanet(tamanho, cor):

    color(cor)
    pendown()
    begin_fill()

    circle(tamanho)

    end_fill()
    penup()


def main():

    # Configuração do cenário
    bgcolor("MidnightBlue")
    speed(11)

    print("Bem-vindo ao mundo Galáctico!!!")
    print("Vamos desenhar a sua galáxia!")

    qtd_estrelas = int(input("Quantidade de estrelas individuais: "))
    qtd_estrelas_galaxia = int(input("Quantidade de estrelas em cada galáxia: "))
    qtd_galaxias = int(input("Quantidade de galáxias: "))
    qtd_constelacoes = int(input("Quantidade de constelações: "))

    cores_estrelas = ["white", "blue", "green", "gray"]

    # Desenha estrelas individuais
    for star in range(qtd_estrelas):
        moveToRandomLocalization()
        drawStar(randint(5, 25), choice(cores_estrelas))

    # Desenha galáxias
    for galaxy in range(qtd_galaxias):
        drawGalaxy(qtd_estrelas_galaxia)

    # Desenha constelações
    for constellation in range(qtd_constelacoes):
        drawConstellation(randint(4, 7))

    hideturtle()
    done()


if __name__ == "__main__":
    main()
