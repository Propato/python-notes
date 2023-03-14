class Window:
    __width = 0 #largura
    __height = 0 #altura
    __color = (255, 0, 255) #cor

    '''
    Vermelho é representado como (255, 0, 0);
    Verde é representado como (0, 255, 0)
    Azul é representado como (0, 0, 255)
    '''

    def __init__(self, largura, altura): #construtor
        self.__width = largura
        self.__height = altura

    def returnWinSize(self): #retorna tamanho da tela
        return (self.__width, self.__height)

    def returnColor(self): #retorna a cor da janela
        return self.__color