from random import randrange, seed
from turtle import *
from freegames import floor, square

bombas = {}

revelado = {}

end = 0

contagens = {}

def inicializar():
    for x in range(-limite, limite, 50):
        for y in range(-limite, limite, 50):
            bombas[x, y] = False
            revelado[x, y] = False
            contagens[x, y] = -1
    if dificuldade == "1":
        num_bombas = 8
    elif dificuldade == "2":
        num_bombas = 16
    elif dificuldade == "3":
        num_bombas = 24
    colocadas = 0
    while colocadas < num_bombas:
        x = randrange(-limite, limite, 50)
        y = randrange(-limite, limite, 50)
        if not bombas[x, y]:
            bombas[x, y] = True
            colocadas += 1
    for x in range(-limite, limite, 50):
        for y in range(-limite, limite, 50):
            total = 0

            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombas.get((x + i, y + j), False)
                    #o get verifica o valor padrao da chave de um dicionario, no caso, o dicionario com nome bombas aqui ta sendo verificado, bizarro.
            contagens[x, y] = total
    update()
def carimbar(x, y, texto):
    square(x, y, 50, 'white')
    color('black')
    penup()
    goto(x + 25, y + 10) 
    write(texto, align="center", font=('Arial', 24, 'normal'))
    pendown()
    #essa função eu peguei de uma atividade anterior e modifiquei um pouco pra caber no contexto do código, o "align" é essencial, não tirem, o codigo nao funciona sem
def desenhar_tabuleiro():
    for x in range(-limite, limite, 50):
        for y in range(-limite, limite, 50):
            carimbar(x, y, "-")
def fim_de_jogo():
    global end
    for x in range(-limite, limite, 50):
        for y in range(-limite, limite, 50):
            if bombas[x, y]:
                square(x, y, 50, 'red')
                color('black')
                end += 1
                update()          
def clique(x, y):
    if end == 0:
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
                        vizinho = (x + i, y + j)
                        if vizinho in revelado and not revelado[vizinho]:
                            pilha.append(vizinho)
    else:
        pass
dificuldade = input("dificuldade desejada, Fácil(digite 1), Médio(digite 2) ou Difícil(digite 3):")
tamaho = input("tamanho do tabuleiro, 8x8, 12x12 ou 16x16:")
tamanho = int(tamaho.split("x")[0])
#o [0] separa o item referenciado na primeira posição, se for um 12 ele separa os 12, e o split("x") separa o x do texto do input, o int transforma em número
limite = (tamanho * 50) // 2
setup(tamanho*50 + 20, tamanho*50 + 20)
hideturtle()
tracer(False)
inicializar()
desenhar_tabuleiro()
onscreenclick(clique)
mainloop()