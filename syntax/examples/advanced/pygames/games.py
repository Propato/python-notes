import pygame
from Window import Window

'''
https://colab.research.google.com/drive/1Wo_1joBc29aJPyZAYTCluojcmqRSAXAM#scrollTo=e6rkBMLUC3iR
'''

#inicia o programa do pygames
pygame.init()
pygame.font.init() # textos na tela
objeto = pygame.font.Font('nome_arquivo', 64)#importar a fonte
print('certo')

w = Window(1024, 600) #cria objeto janela com dimensões 600x400

win = pygame.display.set_mode(w.returnWinSize()) #inicializa a janela do jogo
pygame.display.set_caption('Nome_do_Jogo')
win.fill(w.returnColor()) #insere a cor na janela

# criamos uma instância do relógio
clock = pygame.time.Clock()

# Desenhando linhas na tela pygame.draw.line(superficie, cor, ponto_inicial, ponto_final, largura)
pygame.draw.line(win, (255,0,0), (0,0), (512,300), 10)
pygame.draw.line(win, (0,255,0), (0,600), (512,300), 10)
pygame.draw.line(win, (0,0,255), (512,300), (1024,600), 10)
pygame.draw.line(win, (255,255,255), (512,300), (1024,0), 10)
pygame.display.update()

# desenhando circulos na tela pygame.draw.circle(superficie, cor, centro, raio)
pygame.draw.circle(win, (127,127,127), (512,300), 150)
pygame.display.update()

# desenhando retangulo na tela pygame.draw.rect(superficie, cor, retangulo)
ret = pygame.Rect((300,300), (424, 150)) # criando um objeto retangulo - pygame.Rect((x,y), (largura, altura))
pygame.draw.rect(win, (255,127,255), ret)
pygame.display.update()

# inicio do game-loop
run = True
while run:
    pygame.display.update() #atualiza a tela
    #chamamos o tick do relógio para 30 fps e armazenamos o delta de tempo (diferença de tempo entre um ciclo e outro)
    clock.tick(30)

    #leitura de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #botão "x" utilizado para fechar janela
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN: #verifica se um botão do mouse foi pressionado
            if event.button == 1:
                print("O botão esquerdo do mouse foi clicado!")
                #superf = objeto.render(text, antialias, cor)
                superf = objeto.render('text', True, (0,0,0))
                win.blit(superf)
                mouseX, mouseY = pygame.mouse.get_pos()
        
        if event.type == pygame.KEYDOWN: #verifica se uma tecla foi pressionada

            if event.key == pygame.K_ESCAPE: #caso a tecla "esc" do teclado tenha sido a tecla pressionada, encerramos o loop/jogo
                run = False
            elif event.key == pygame.K_LEFT:
                print("←")
            elif event.key == pygame.K_RIGHT:
                print("→")
            elif event.key == pygame.K_UP:
                print("↑")
            elif event.key == pygame.K_DOWN:
                print("↓")


# event.button == 1 => botão esquerdo
# event.button == 2 => botão do scroll
# event.button == 3 => botão direito
# event.button == 4 => qualquer botão

pygame.font.quit()
pygame.quit()