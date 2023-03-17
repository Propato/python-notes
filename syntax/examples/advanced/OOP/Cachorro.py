# SubClasse de Animal

from Animals import Animal

class Cachorro (Animal):
    
    def __init__(self, nome, cor, comida, sexo): # o __ define a propriedade como privada
        super().__init__(nome, cor, comida) 
        self.__sexo = sexo

    def __str__(self):
        if(self.__sexo == 'F' or self.__sexo == 'f'):
            descricao = f"A cachorra {self.nome} é da cor {self.cor}, e gosta muito de comer {self.comida}"
        if(self.__sexo == 'M' or self.__sexo == 'm'):
            descricao = f"O cachorro {self.nome} é da cor {self.cor}, e gosta muito de comer {self.comida}"
        return descricao