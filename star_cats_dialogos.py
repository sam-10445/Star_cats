import pygame
pygame.init()
pygame.display.set_caption("Star Cats")#a
janela = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

mouse_x, mouse_y = 0,0
tela_sena_inicial = False
tela_mapa = False
tela_dialogo=False
tela_loja=False
tela_boss_1=False
tela_boss_2=False
tela_boss_3=False
#controle de passagem de diálogos
passar = 0
passar_passaro = 0
passar_peixe = 0
passar_cao = 0

# CARREGAMENTO DAS IMAGENS
#menu
menu = pygame.image.load('imagens/menu.jpg')
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

#sena inicial
sena_inicial = pygame.image.load('imagens/sena_inicial.jpg')
sena_inicial = sena_inicial.convert()
sena_inicial = pygame.transform.scale(sena_inicial, (1000, 700))

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

#FUNÇÕES:

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

#DIÁLOGOS:
#texto inicial:
font = pygame.font.Font(None, 30) 
texto_inicial = font.render(f"Parece que não foi uma boa ideia pescar durante uma tempestade.", True, 'black')
texto_inicial1 = font.render(f"Você naufragou em uma ilha desconhecida...", True, 'black')
texto_inicial2 = font.render(f"Ela parece meio abandonada.", True, 'black')
texto_inicial3 = font.render(f"Percebe que algo importante não está mais com você.", True, 'black')
#dialogo_loja
font = pygame.font.Font(None, 30) 
dialogo_loja = font.render(f"Pegue tudo que precisa. Mas lembre-se que tudo tem um preço.", True, 'black')
#primeiro_dialogo:
font = pygame.font.Font(None, 30) 
primeiro_dialogo1 = font.render(f"Uma estrela? Isso não é algo comum de se perder.", True, 'black')
primeiro_dialogo2 = font.render(f"Vou ser honesto: não sei onde ela está.", True, 'black')
primeiro_dialogo3 = font.render(f"Mas talvez eu tenha uma pista.", True, 'black')
primeiro_dialogo4 = font.render(f"Ao norte da ilha vive um cão… ele coleciona tudo que acha valioso.", True, 'black')
primeiro_dialogo5 = font.render(f"Se encontrou sua estrela, pode ter certeza de que ficou com ela.", True, 'black')
primeiro_dialogo6 = font.render(f"O problema é chegar até lá.", True, 'black')
primeiro_dialogo7 = font.render(f"O lugar é fechado por dois cadeados, e nisso eu não posso ajudar.", True, 'black')
primeiro_dialogo8 = font.render(f"Talvez o pássaro ao norte saiba de algo.", True, 'black')
primeiro_dialogo9 = font.render(f"Ah, e se precisar de uma “ajudinha”", True, 'black')
primeiro_dialogo10 = font.render(f"o comerciante no centro da ilha vende coisas bem interessantes.", True, 'black')
primeiro_dialogo11 = font.render(f"Boa sorte, visitante.", True, 'black')
#dialogo_passaro:
font = pygame.font.Font(None, 30) 
dialogo_passaro1 = font.render(f"Uma estrela?", True, 'black')
dialogo_passaro2 = font.render(f"E desde quando gato precisa disso, hein?", True, 'black')
dialogo_passaro3 = font.render(f"Olha, gatinho, não vi nenhuma estrela passeando por aí.", True, 'black')
dialogo_passaro4 = font.render(f"E a ilha nem é tão grande assim.", True, 'black')
dialogo_passaro5 = font.render(f"Mas se ela existe…", True, 'black')
dialogo_passaro6 = font.render(f"provavelmente está naquela casa fedida de cachorro no norte da ilha.", True, 'black')
dialogo_passaro7 = font.render(f"Trancada? Claro que está!", True, 'black')
dialogo_passaro8 = font.render(f"Dois cadeados… que chato, né? kk.", True, 'black')
dialogo_passaro9 = font.render(f" Eu tenho uma das chaves.", True, 'black')
dialogo_passaro10 = font.render(f"  Mas não pense que vou dar de graça.", True, 'black')
dialogo_passaro11 = font.render(f"Que tal uma batalha?", True, 'black')
dialogo_passaro12 = font.render(f"Ou vai me dizer que está com medo?", True, 'black')
dialogo_passaro13 = font.render(f"Se vencer, a chave é sua!", True, 'black')
#dialogo_peixe
font = pygame.font.Font(None, 30) 
dialogo_peixe1 = font.render(f"…Uma estrela?", True, 'black')
dialogo_peixe2 = font.render(f"Não… não a vi", True, 'black')
dialogo_peixe3 = font.render(f"Afinal, como um peixe veria uma estrela debaixo da água?", True, 'black')
dialogo_peixe4 = font.render(f"Mas se for algo tão precioso assim,", True, 'black')
dialogo_peixe5 = font.render(f"deve estar onde todas as coisas preciosas acabam indo…", True, 'black')
dialogo_peixe6 = font.render(f"para a casa do cachorro ao norte da ilha.", True, 'black')
dialogo_peixe7 = font.render(f"Ele não é nada amigável, pelo menor, não mais.", True, 'black')
dialogo_peixe8 = font.render(f"Esta chave…é tudo o que me restou dos bons tempos.", True, 'black')
dialogo_peixe9 = font.render(f"Você a quer, não é? Então fique um pouco comigo.", True, 'black')
dialogo_peixe10 = font.render(f"Que tal um jogo?", True, 'black')
dialogo_peixe11 = font.render(f"A chave será sua se aceitar.", True, 'black')
#dialogo_cao
font = pygame.font.Font(None, 30) 
dialogo_cao1 = font.render(f"Estrela? Ah, sim, eu que encontrei, agora ela é minha.", True, 'black')
dialogo_cao2 = font.render(f"Só não sei o que um gatinho assustado está fazendo aqui…", True, 'black')
dialogo_cao3 = font.render(f"Pensei que os cadeados e os ossos já tivessem deixado bem claro", True, 'black')
dialogo_cao4 = font.render(f"que este não é um lugar para algo tão minúsculo como você.", True, 'black')
dialogo_cao5 = font.render(f"Olhe só para você! ", True, 'black')
dialogo_cao6 = font.render(f"Passeando pela ilha e pegando chaves por uma estrela boba!", True, 'black')
dialogo_cao7 = font.render(f"Na verdade eu nem gostei dela, achei que era de verdade", True, 'black')
dialogo_cao8 = font.render(f"mas não passa de um brinquedinho de pelúcia velho.", True, 'black')
dialogo_cao9 = font.render(f"Não me diga que era de quando você era um filhotinho?", True, 'black')
dialogo_cao10 = font.render(f"Deve ter um grande valor pra você né?", True, 'black')
dialogo_cao11 = font.render(f"Agora que sei que é tão importante, vou ficar com ela.", True, 'black')
dialogo_cao12 = font.render(f"Agora ela é minha, entendeu?", True, 'black')
dialogo_cao13 = font.render(f"Uh? Você quer batalhar por ela? ", True, 'black')
dialogo_cao14 = font.render(f"Um gatinho contra um cão?", True, 'black')
dialogo_cao15 = font.render(f"Hahahahaha", True, 'black')
dialogo_cao16 = font.render(f"Porque não? Vamos começar?", True, 'black')

#CONTROLES (orientação)
font = pygame.font.Font(None, 25) 
#pular dialogo
pular_dialogo_gato = font.render(f"Próximo: tecla g", True, 'black')
pular_dialogo_passaro = font.render(f"Próximo: tecla 1", True, 'black')
pular_dialogo_peixe = font.render(f"Próximo: tecla 2", True, 'black')
pular_dialogo_cao = font.render(f"Próximo: tecla 3", True, 'black')
#voltar ao mapa
voltar_ao_mapa = font.render(f"Voltar ao mapa: m", True, 'black')

#QUADRADOS DAS CASAS
quadrado = pygame.Surface([30, 30]) # cria quadrado com 30 pixels de lado
quadrado_0= pygame.Rect(141, 283, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_1 = pygame.Rect(105, 20, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_2 =pygame.Rect(850, 456, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_3 = pygame.Rect(603,120, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_4 = pygame.Rect(512,350, 30, 30) # cria quadrado com 30 pixels de lado

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #apertar o X
      pygame.quit()
    if event.type == pygame.MOUSEMOTION: #MOVER O MOUSE
      mouse_x = event.pos[0]
      mouse_y = event.pos[1]
    if event.type == pygame.KEYDOWN: #APERTAR TECLAS
        if event.key == pygame.K_RETURN: #apertar o ENTER
            tela_sena_inicial = True
        if event.key == pygame.K_m: #apertar "m" ou "M"
            tela_mapa = True
        if event.key == pygame.K_g: #aperta g (passar dialogo gato)
                passar += 1
        if event.key == pygame.K_1: #apertar 1 (passar dialogo passaro)
                passar_passaro += 1
        if event.key == pygame.K_2: #apertar 2 (passar dialogo peixe)
                passar_peixe += 1
        if event.key == pygame.K_3: #apertar 3 (passar dialogo cão)
                passar_cao += 1
        

  #PARTE 1: MENU
  janela.blit(menu, (0, 0))

  #PARTE 2: CENA INICIAL
  if tela_sena_inicial == True: 
    janela.fill((255, 255, 255))
    janela.blit(sena_inicial, (0, 0))
    janela.blit(texto_inicial, (200, 610))
    janela.blit(texto_inicial1, (200, 630))
    janela.blit(texto_inicial2, (200, 650))
    janela.blit(texto_inicial3, (200, 670))

  #PARTE 3: MAPA
  if tela_mapa == True: 
    ##NO MAPA: 
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
    #
    quadrado.fill((225, 0, 0))
    janela.blit(quadrado, quadrado_0) #cordenadas botão_0
    janela.blit(quadrado, quadrado_1) #cordenadas botão_1
    janela.blit(quadrado, quadrado_2) #cordenadas botão_2
    janela.blit(quadrado, quadrado_3)#cordenadas botão_3
    janela.blit(quadrado, quadrado_4)#cordenadas botão_3
    janela.blit(black, (mouse_x, mouse_y))
    #quadrado branco de fundo de diálogo
    quadrado_dialogo = pygame.Surface([1000, 40])
    quadrado_dialogo.fill((225, 225, 225))

  #PARTE 3: TELA DE BOSS E DIÁLOGOS
  if event.type == pygame.MOUSEBUTTONDOWN:#detecta evento tipo mouse
    if event.button == 1 and tela_mapa:#diz que o botão a ser apertado tem que ser o esquerdo do mouse e que só pode ser apertado no mapa
        if quadrado_0.collidepoint(event.pos):
          tela_dialogo=True
        elif quadrado_1.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_boss_1=True
        elif quadrado_2.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_boss_2=True
        elif quadrado_3.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_boss_3=True
        elif quadrado_4.collidepoint(event.pos):#verifica se o botão clicado colidiu com o quadrado.
          tela_loja=True

  if tela_dialogo==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(dialogo_1, (0, 0))
    #DIÁLOGO
    #colocar os controles (orientação)
    janela.blit(pular_dialogo_gato, (715, 30)) 
    janela.blit(voltar_ao_mapa, (700, 50)) 
    #passar dialogo
    if passar == 0:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo1, (200, 650)) 
    elif passar == 1:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo2, (200, 650)) 
    elif passar == 2:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo3, (200, 650)) 
    elif passar == 3:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo4, (200, 650)) 
    elif passar == 4:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo5, (200, 650)) 
    elif passar == 6:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo6, (200, 650)) 
    elif passar == 7:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo7, (200, 650)) 
    elif passar == 8:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo8, (200, 650)) 
    elif passar == 9:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo9, (200, 650)) 
    elif passar == 10:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo10, (200, 650)) 
    elif passar == 11:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(primeiro_dialogo11, (200, 650)) 
    elif passar > 11:
        tarefa = 2

  if tela_loja==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(loja, (0, 0))
    #DIÁLOGO
    janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
    janela.blit(dialogo_loja, (200, 650)) 

  if tela_boss_1==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(passaro, (0, 0))
    #DIÁLOGO
    #colocar os controles (orientação)
    janela.blit(pular_dialogo_passaro, (715, 30)) 
    janela.blit(voltar_ao_mapa, (700, 50)) 
    #passar dialogo
    if passar_passaro == 0:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro1, (200, 650)) 
    elif passar_passaro == 1:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro2, (200, 650)) 
    elif passar_passaro == 2:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro3, (200, 650)) 
    elif passar_passaro == 3:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro4, (200, 650)) 
    elif passar_passaro == 4:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro5, (200, 650)) 
    elif passar_passaro == 5:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro6, (200, 650)) 
    elif passar_passaro == 6:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro7, (200, 650)) 
    elif passar_passaro == 7:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro8, (200, 650)) 
    elif passar_passaro == 8:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro9, (200, 650)) 
    elif passar_passaro == 9:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro10, (200, 650)) 
    elif passar_passaro == 10:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro11, (200, 650)) 
    elif passar_passaro == 11:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro12, (200, 650)) 
    elif passar_passaro == 12:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_passaro13, (200, 650)) 
    elif passar_passaro > 12:
        tarefa = 3

  if tela_boss_2==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(peixe, (0, 0))
    #DIÁLOGO
    #colocar os controles (orientação)
    janela.blit(pular_dialogo_peixe, (715, 30)) 
    janela.blit(voltar_ao_mapa, (700, 50)) 
    #passar dialogo
    if passar_peixe == 0:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe1, (200, 650)) 
    elif passar_peixe == 1:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe2, (200, 650)) 
    elif passar_peixe == 2:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe3, (200, 650)) 
    elif passar_peixe == 3:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe4, (200, 650)) 
    elif passar_peixe == 4:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe5, (200, 650)) 
    elif passar_peixe == 5:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe6, (200, 650)) 
    elif passar_peixe == 6:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe7, (200, 650)) 
    elif passar_peixe == 7:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe8, (200, 650)) 
    elif passar_peixe == 8:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe9, (200, 650)) 
    elif passar_peixe == 9:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe10, (200, 650)) 
    elif passar_peixe == 10:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_peixe11, (200, 650)) 
    elif passar_peixe > 10:
        tarefa = 4

  if tela_boss_3==True:
    janela.fill((255, 255, 255)) # apaga o quadro atual
    janela.blit(cao, (0, 0))
    #DIÁLOGO
    #colocar os controles (orientação)
    janela.blit(pular_dialogo_cao, (715, 30)) 
    janela.blit(voltar_ao_mapa, (700, 50)) 
    #passar dialogo
    if passar_cao == 0:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao1, (200, 650)) 
    elif passar_cao == 1:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao2, (200, 650)) 
    elif passar_cao == 2:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao3, (200, 650)) 
    elif passar_cao == 3:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao4, (200, 650)) 
    elif passar_cao == 4:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao5, (200, 650)) 
    elif passar_cao == 5:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao6, (200, 650)) 
    elif passar_cao == 6:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao7, (200, 650)) 
    elif passar_cao == 7:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao8, (200, 650)) 
    elif passar_cao == 8:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao9, (200, 650)) 
    elif passar_cao == 9:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao10, (200, 650)) 
    elif passar_cao == 10:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao11, (200, 650)) 
    elif passar_cao == 11:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao12, (200, 650)) 
    elif passar_cao == 12:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao13, (200, 650)) 
    elif passar_cao == 13:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao14, (200, 650)) 
    elif passar_cao == 14:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao15, (200, 650)) 
    elif passar_cao == 15:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_cao16, (200, 650)) 

  pygame.display.flip() # Desenha o quadro atual na tela
  clock.tick(60)