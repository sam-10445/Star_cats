import pygame
import pygame as pg 
pygame.init()
pygame.display.set_caption("Star Cats")#a
janela = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

mouse_x, mouse_y = 0,0
tela_mapa = False
tela_dialogo=False
tela_loja=False
tela_boss_1=False
tela_boss_2=False
tela_boss_3=False

# CARREGAMENTO DAS IMAGENS
#menu
menu = pygame.image.load('imagens/menu.png')
menu = menu.convert()
menu = pygame.transform.scale(menu, (1000, 700))

#black (sem fundo)
black = pygame.image.load('imagens/black_sem_fundo.png')
black = black.convert_alpha()
black = pygame.transform.scale(black, (62,45))
black = pygame.transform.flip(black, True, False) #imagem, inverter horizontalmente?, inverter verticalmente?

#mapa
mapa = pygame.image.load('imagens/mapa.png') 
mapa = mapa.convert_alpha()
mapa = pygame.transform.scale(mapa, (1000, 700))

#primeiro dialogo
dialogo_1 = pygame.image.load('imagens/conversa_gato.png')
dialogo_1 = dialogo_1.convert()
dialogo_1 = pygame.transform.scale(dialogo_1, (1000, 700))
#passaro
passaro = pygame.image.load('imagens/passaro.png')
passaro = passaro.convert()
passaro = pygame.transform.scale(passaro, (1000, 700))

#peixe
peixe = pygame.image.load('imagens/peixe.png')
peixe.convert()
peixe = pygame.transform.scale(peixe, (1000, 700))

#cao
cao = pygame.image.load('imagens/cao.png')
cao.convert()
cao = pygame.transform.scale(cao, (1000, 700))

#loja
loja = pygame.image.load('imagens/loja.png')
loja.convert()
loja = pygame.transform.scale(loja, (1000, 700))

#tela de derrota
tela_de_derrota = pygame.image.load('imagens/tela_de_derrota.png')
tela_de_derrota.convert()
tela_de_derrota = pygame.transform.scale(tela_de_derrota, (1000, 700))

#tela de vitoria
tela_de_vitoria = pygame.image.load('imagens/tela_de_vitoria.png')
tela_de_vitoria.convert()
tela_de_vitoria = pygame.transform.scale(tela_de_vitoria, (1000, 700))

#mouse (sem fundo)
mouse = pygame.image.load('imagens/mouse_sem_fundo.png')
mouse = mouse.convert_alpha()
mouse = pygame.transform.scale(mouse, (52,35))

#ITENS (com fundo)
#leite
leite = pygame.image.load('imagens/iten_leite.png')
leite = leite.convert()
leite = pygame.transform.scale(leite, (25.6,26.3))

#sardinha
sardinha = pygame.image.load('imagens/iten_sardinha.png')
sardinha = sardinha.convert()
sardinha = pygame.transform.scale(sardinha, (35.8, 33.3))

#biscoito de peixe
biscoito_de_peixe = pygame.image.load('imagens/iten_peixe.png')
biscoito_de_peixe = biscoito_de_peixe.convert()
biscoito_de_peixe = pygame.transform.scale(biscoito_de_peixe, (30, 22.1))

#PATAS (sem fundo)
#pata preta
pata_preta = pygame.image.load('imagens/pata_preta_sem_fundo.png')
pata_preta = pata_preta.convert_alpha()
pata_preta = pygame.transform.scale(pata_preta, (220, 209))

#pata azul
pata_azul = pygame.image.load('imagens/pata_azul_sem_fundo.png')
pata_azul = pata_azul.convert_alpha()
pata_azul = pygame.transform.scale(pata_azul, (211.5, 209))

#pata vermelha
pata_vermelha = pygame.image.load('imagens/pata_vermelha_sem_fundo.png')
pata_vermelha = pata_vermelha.convert_alpha()
pata_vermelha = pygame.transform.scale(pata_vermelha, (195.5, 209))

quadrado = pygame.Surface([30, 30]) # cria quadrado com 30 pixels de lado
quadrado_0= pygame.Rect(141, 283, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_1 = pygame.Rect(105, 20, 30, 30)
quadrado_2 =pygame.Rect(850, 456, 30, 30)
quadrado_3 = pygame.Rect(603,120, 30, 30)
quadrado_4 = pygame.Rect(512,350, 30, 30) # cria quadrado com 30 pixels de lado
font = pygame.font.Font(None, 24) #definir fonte
surface_texto = font.render(f"Aperte enter", True, 'black')
pos=((141, 283))
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    elif event.type == pygame.MOUSEMOTION:
      mouse_x = event.pos[0]
      mouse_y = event.pos[1]
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:  # tecla de espaço
        tela_mapa = True

      #CLICAR NOS QUADRADOS VERMELHOS
      '''for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
          pg.quit()
          sys.exit()
        elif event.type == pg.MOUSEBUTTONUP: # trata liberação do botão do mouse
          posicao_clique = event.pos  # coordenadas do ponteiro do mouse
          # verifica se jogador clicou no bloco aceso
          if alvo is not None and alvo.rect.collidepoint(posicao_clique):
            alvo.apagar()
            alvo = None
            contagem += 1'''

  #quadrado.fill((225, 0, 0))         # preenche o quadrado com cor branca
  #janela.blit(quadrado, (50, 200)) # desenha o quadrado no quadro atual e nas coordenadas indicadas

  #PARTE 1: MENU
  janela.blit(menu, (0, 0))

  #PARTE 2: MAPA
  if tela_mapa == True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(mapa, (0, 0))
    janela.blit(black, (mouse_x, mouse_y))
    quadrado.fill((225, 0, 0))
    janela.blit(quadrado, quadrado_0) #cordenadas botão_0
    janela.blit(quadrado, quadrado_1) #cordenadas botão_1
    janela.blit(quadrado, quadrado_2) #cordenadas botão_2
    janela.blit(quadrado, quadrado_3)#cordenadas botão_3
    janela.blit(quadrado, quadrado_4)#cordenadas botão_3

  if event.type == pygame.MOUSEBUTTONDOWN:#detecta evento tipo mouse
    if event.button == 1 and tela_mapa:#diz que o botão a ser apertado tem que ser o esquerdo do mouse e que só pode ser apertado no mapa
        if quadrado_0.collidepoint(event.pos):
          tela_mapa= False
          tela_dialogo=True
        elif quadrado_1.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_mapa = False
          tela_boss_1=True
        elif quadrado_2.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_mapa = False
          tela_boss_2=True
        elif quadrado_3.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_mapa = False
          tela_boss_3=True
        elif quadrado_4.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_mapa = False
          tela_loja=True
  if tela_dialogo==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(dialogo_1, (0, 0))
  
  if tela_loja==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(loja, (0, 0))

  if tela_boss_1==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(passaro, (0, 0))

  if tela_boss_2==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(peixe, (0, 0))

  if tela_boss_3==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(cao, (0, 0))

  pygame.display.flip() # Desenha o quadro atual na tela
  clock.tick(60)
