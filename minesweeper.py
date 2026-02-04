from random import randrange, seed
from turtle import *

from freegames import floor, square

# -------------------------------------------------
# Configuração da aleatoriedade
# -------------------------------------------------

seed(0)


# -------------------------------------------------
# Estruturas de dados do jogo
# -------------------------------------------------

# Indica se existe uma bomba em cada posição (x, y)
bombas = {}

# Indica se a célula já foi revelada
revelado = {}

# Armazena a quantidade de bombas vizinhas
contagens = {}


# -------------------------------------------------
# Inicialização do tabuleiro
# -------------------------------------------------

def inicializar():
    """
    Inicializa o tabuleiro do jogo.
    """

    # Inicializa as estruturas de dados (variáveis)
    # que representa o estado do tabuleiro.
    # Para cada célula:
    # - bombas[(x, y)] com False (não tem bomba)
    # - revelado[(x, y)] com False (não está revelado)
    # - contagens[(x, y)] com um -1 (sem bomba ao redor)
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombas[x, y] = False
            revelado[x, y] = False
            contagens[x, y] = -1

    # Posiciona as bombas aleatoriamente
    num_bombas = 12
    colocadas = 0
    while colocadas < num_bombas:
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        if not bombas[x, y]:
            bombas[x, y] = True
            colocadas += 1

    # Calcula a quantidade de bombas vizinhas
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            total = 0

            # Verifica a célula atual e as vizinhas
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombas[x + i, y + j]

            contagens[x, y] = total


# -------------------------------------------------
# Funções de desenho
# -------------------------------------------------

def carimbar(x, y, texto):
    """Desenha uma célula com um texto."""
    square(x, y, 50, 'white')
    color('black')
    write(texto, font=('Arial', 50, 'normal'))


def desenhar_tabuleiro():
    """
    Desenha o tabuleiro inicial, com todas as
    células marcadas como desconhecidas.
    """
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            carimbar(x, y, "?")


def fim_de_jogo():
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombas[x, y]:
                carimbar(x, y, "X")
    #fazendo com que todas as bombas sejam exibidas em X


# -------------------------------------------------
# Interação com o jogador
# -------------------------------------------------

def clique(x, y):
    """
    Responde ao clique do mouse.
    """

    # Ajusta as coordenadas do clique para a grade
    x = floor(x, 50)
    y = floor(y, 50)

    # Se o jogador clicou em uma bomba, o jogo termina
    if bombas[x, y]:
        fim_de_jogo()
        return
        

    # Lista de células que ainda precisam ser processadas
    pilha = [(x, y)]

    while pilha:
        x, y = pilha.pop()

        # Revela a célula atual
        carimbar(x, y, contagens[x, y])
        revelado[x, y] = True

        # Se não houver bombas vizinhas,
        # revela automaticamente as células ao redor
        if contagens[x, y] == 0:
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    vizinho = x + i, y + j

                    if not revelado[vizinho]:
                        pilha.append(vizinho)


# -------------------------------------------------
# Configuração da janela e início do jogo
# -------------------------------------------------
jogador = input("Nome do jogador:")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

inicializar()
desenhar_tabuleiro()

onscreenclick(clique)
mainloop()


