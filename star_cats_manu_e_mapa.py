import pygame
import pygame as pg 
pygame.init()
pygame.display.set_caption("Star Cat")
janela = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

mouse_x, mouse_y = 0,0
tela_mapa = False

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

#quadrado = pygame.Surface([30, 30]) # cria quadrado com 30 pixels de lado
font = pygame.font.Font(None, 24) #definir fonte
surface_texto = font.render(f"Aperte enter", True, 'black')

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



  pygame.display.flip() # Desenha o quadro atual na tela
  clock.tick(60)
