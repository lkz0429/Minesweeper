from random import randrange, seed
from turtle import *
from freegames import floor, square

seed(0)

bombas = {}

revelado = 0

contagens = {}

def inicializar():
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombas[x, y] = False
            contagens[x, y] = -1
    if dificuldade == "Fácil":
        num_bombas = 4
    elif dificuldade == "Médio":
        num_bombas = 8
    elif dificuldade == "Difícil":
        num_bombas = 12
    colocadas = 0
    while colocadas < num_bombas:
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        if not bombas[x, y]:
            bombas[x, y] = True
            colocadas += 1
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            total = 0

            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombas[x + i, y + j]
            contagens[x, y] = total
    update()
def parar():
    return
def carimbar(x, y, texto):
    square(x, y, 50, 'white')
    color('black')
    penup()
    goto(x + 25, y + 10) 
    write(texto, align="center", font=('Arial', 24, 'normal'))
    pendown()
    #essa função eu peguei de uma atividade anterior e modifiquei um pouco pra caber no contexto do código, o "align" é essencial, não tirem !!!
def desenhar_tabuleiro():
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            carimbar(x, y, "-")
def fim_de_jogo():
    global revelado
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombas[x, y]:
                square(x, y, 50, 'red')
                color('black')
                revelado += 1
                
            
def clique(x, y):
    if revelado == 0:
        x = floor(x, 50)
        y = floor(y, 50)
        if bombas[x, y]:
            fim_de_jogo()
            return
        pilha = [(x, y)]
        while pilha:
            x, y = pilha.pop()
            carimbar(x, y, contagens[x, y])
            revelado[x, y] = True
            if contagens[x, y] == 0:
                for i in (-50, 0, 50):
                    for j in (-50, 0, 50):
                        vizinho = x + i, y + j
                        if not revelado[vizinho]:
                            pilha.append(vizinho)
    else:
        pass
jogador = input("Nome do jogador:")
dificuldade = input("digite aqui a dificuldade desejada, Fácil, Médio ou Difícil:")
tamaho = input("digite o tamanho do tabuleiro, 8x8, 12x12 ou 16x16:")
setup(420, 420, 0, 70)
hideturtle()
tracer(False)
inicializar()
desenhar_tabuleiro()
onscreenclick(clique)
mainloop()


