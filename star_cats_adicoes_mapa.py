import pygame
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

#rosa dos ventos (sem fundo)
rosa = pygame.image.load('imagens/rosa_dos_ventos_sem_fundo.png')
rosa = rosa.convert_alpha()
rosa = pygame.transform.scale(rosa, (109,109))

#mapa
mapa = pygame.image.load('imagens/mapa.png') 
mapa = mapa.convert_alpha()
mapa = pygame.transform.scale(mapa, (1000, 700))

#primeiro dialogo
dialogo_1 = pygame.image.load('imagens/conversa_gato.jpg')
dialogo_1 = dialogo_1.convert()
dialogo_1 = pygame.transform.scale(dialogo_1, (1000, 700))

#passaro
passaro = pygame.image.load('imagens/passaro.png')
passaro = passaro.convert()
passaro = pygame.transform.scale(passaro, (1000, 700))

#peixe
peixe = pygame.image.load('imagens/peixe_batalha.png')
peixe.convert()
peixe = pygame.transform.scale(peixe, (1000, 700))

#cao
cao = pygame.image.load('imagens/cao.png')
cao.convert()
cao = pygame.transform.scale(cao, (1000, 700))

#loja
loja = pygame.image.load('imagens/loja.jpg')
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

#STATUS: (dinheiro, chaves)
#status de dinheiro:
dinheiro = 300
font = pygame.font.Font(None, 30) #definir fonte
status_dinheiro = font.render(f"Dinheiro: R${dinheiro}", True, 'black')
#quantidade de chaves:
chaves = 0
font = pygame.font.Font(None, 30) #definir fonte
status_chaves = font.render(f"Chaves: {chaves}/2", True, 'black')
#quantidade de vidas restantes
vidas = 1
font = pygame.font.Font(None, 30) #definir fonte
status_vidas = font.render(f"Vidas restantes: {vidas}", True, 'black')

#BARRA DE TAREFAS
tarefa = 1
#título
font = pygame.font.Font(None, 30) #definir fonte
titulo = font.render(f"OBJETIVO:", True, 'black')
#tarefa 1
font = pygame.font.Font(None, 22) #definir fonte
tarefa1 = font.render(f"* Ir para a 1º casa azul ao oeste", True, 'black')
tarefa1_1 = font.render(f"(talvez consiga alguma informação)", True, 'black')
#tarefa 2
font = pygame.font.Font(None, 22) #definir fonte
tarefa2 = font.render(f"* Ir para a casa de pássaro ao norte", True, 'black')
#tarefa 3
font = pygame.font.Font(None, 22) #definir fonte
tarefa3 = font.render(f"* Ir para o lago do leste da ilha", True, 'black')
#tarefa 4
font = pygame.font.Font(None, 22) #definir fonte
tarefa4 = font.render(f"* Ir para a casa do cão ao norte da ilha", True, 'black')
tarefa4_1 = font.render(f"(É hora da batalha final)", True, 'black')

#QUADRADOS DAS CASAS
quadrado = pygame.Surface([30, 30]) # cria quadrado com 30 pixels de lado
quadrado_0= pygame.Rect(141, 283, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_1 = pygame.Rect(105, 20, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_2 =pygame.Rect(850, 456, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_3 = pygame.Rect(603,120, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_4 = pygame.Rect(512,350, 30, 30) # cria quadrado com 30 pixels de lado

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    elif event.type == pygame.MOUSEMOTION:
      mouse_x = event.pos[0]
      mouse_y = event.pos[1]
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:  
        tela_mapa = True

  #PARTE 1: MENU
  janela.blit(menu, (0, 0))

  #PARTE 2: MAPA
  if tela_mapa == True: 
    #NO MAPA: 
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(mapa, (0, 0)) #desenhar mapa
    janela.blit(rosa, (850, 10)) #desenhar rosa dos ventos
    #STATUS:
    janela.blit(status_dinheiro, (10, 650)) #status dinheiro
    janela.blit(status_chaves, (10, 630)) #quantidade de chaves
    janela.blit(status_vidas, (10, 610)) #quantidade de vidas
    #
    #BARRA DE TAREFAS:
    janela.blit(titulo, (725, 130)) #tarefa1
    if tarefa == 1:
        janela.blit(tarefa1, (725, 160)) #tarefa1
        janela.blit(tarefa1_1, (725, 180)) #tarefa1_1
    elif tarefa == 2:
        janela.blit(tarefa2, (725, 160)) #tarefa2
    elif tarefa == 3:
        janela.blit(tarefa3, (725, 160)) #tarefa3
    elif tarefa == 4:
        janela.blit(tarefa4, (725, 160)) #tarefa4
        janela.blit(tarefa4_1, (725, 180)) #tarefa4
    quadrado.fill((225, 0, 0))
    janela.blit(quadrado, quadrado_0) #cordenadas botão_0
    janela.blit(quadrado, quadrado_1) #cordenadas botão_1
    janela.blit(quadrado, quadrado_2) #cordenadas botão_2
    janela.blit(quadrado, quadrado_3)#cordenadas botão_3
    janela.blit(quadrado, quadrado_4)#cordenadas botão_3
    janela.blit(black, (mouse_x, mouse_y))

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
  if event.type== pygame.KEYDOWN:#tentativa de um possivel retorno do jogador para tela inicial.
    if event.key == pygame.K_ESCAPE:#indentidica se a tecla apertada é esc
      tela_mapa==True
      tela_loja= False
      tela_dialogo=False
      tela_boss_1=False
      tela_boss_2=False
      tela_boss_3=False

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