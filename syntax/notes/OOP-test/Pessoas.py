class Pessoa:

    def __init__(self, nome, idade, cpf, numero):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.numero = numero
        self.time = 'time_não_inserido'

    def __str__(self):
        return f"N {self.numero}: {self.nome}, de {self.idade}, com o cpf {self.cpf}, pertence ao time {self.time.nome}."

    def setTime(self, time):
        self.time = time