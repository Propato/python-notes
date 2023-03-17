# SuperClasse Animal

class Animal:
    """
    Propriedades:
        nome : nome do animal (string)
        cor : nome da cor (string)
        comida : nome do alimento que ele consome (string)
    """
    def __init__(self, nome, cor, comida): # o __ define a propriedade como privada
        self.__nome = nome
        self.__cor = cor
        self.__comida = comida
    
    def __str__(self):
        descricao = f"{self.__nome} é da cor {self.__cor}, e gosta muito de comer {self.__comida}"
        return descricao
    
    def comer(self):
      print(f"{self.__nome} está comendo {self.__comida}.")
    
    def movimento(self):
      print(f"{self.__nome} vive correndo por aí.")

    # @property configura os getters podendo acessar normalmente o valor de uma variavel privada

    @property
    def nome(self):
        return self.__nome

    @property
    def cor(self):
        return self.__cor

    @property
    def comida(self):
        return self.__comida


    # @{nome_variavel}.setter configura os setters podendo modificar normalmente o valor de uma variavel

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @comida.setter
    def comida(self, comida):
        self.__comida = comida