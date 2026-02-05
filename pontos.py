import os
import json

class Test:
    def __init__(self, caminho1) -> None:
        self.caminho = caminho1
        if os.path.exists(caminho1) and os.path.getsize(caminho1)<1:
            self.conteudo = []
        elif not os.path.exists(caminho1):
            self.conteudo = []
        else:
            self.conteudo = json.load(open(caminho1, "r"))
    def add_user(self,jogador):
        self.conteudo.append(jogador)
        arquivo = open(self.caminho, "w",)
        json.dump(self.conteudo, arquivo, indent=8)
        arquivo.close()
        return
    def mostra_jogadores(self):
        print(json.load(open(self.caminho, "r")))