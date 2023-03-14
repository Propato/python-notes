from Pessoas import Pessoa

class Time:

    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def __str__(self):
        return f'O {self.nome} está com tudo!'
    
    def printJogadores(self):
        print(f'O {self.nome} tem {len(self.jogadores)} jogadores, e são eles:', end='\n')
        for i in self.jogadores: 
            print(i)
        print()

    def setJogador(self, jogador):
        self.jogadores.append(jogador)
        jogador.setTime(self)