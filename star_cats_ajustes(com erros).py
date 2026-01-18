import pygame
pygame.init()
pygame.display.set_caption("Star Cats")
janela = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

#VARIAVEIS
#mouse
mouse_x, mouse_y = 0,0

#telas (imagens)
tela_dificuldade = False
tela_sena_inicial = False
tela_mapa = False
tela_dialogo=False
tela_dialogo_passaro = False
tela_dialogo_peixe = False
tela_dialogo_cao = False
tela_loja=False
tela_boss_1=False
tela_boss_2=False
tela_boss_3=False

#telas especiais
abrir_tela_de_chaves = False
abrir_tela_de_derrota = False
abrir_tela_de_vitoria = False
abrir_tela_pontuacao = False
abrir_tela_game_over = False

#controle de passagem de diálogos
passar = 0
pular = 0

#variáveis de status (iniciais)
dificuldade = "fácil"
chaves = 0
vidas = 2
dinheiro = 300

#variaveis das batalhas
tempo = 0

#variaveis da tela de pontuação (black)
nota = 0
nota_passaro = ""
nota_peixe = ""
nota_cao = ""
pontos_black1 = 0 #o valor deve ser zero
pontos_black2 = 0 #o valor deve ser zero
pontos_black3 = 0 #o valor deve ser zero

#controle de batalhas e vitórias
sim = 0
nao = 0
abrir_menu_passaro = False
abrir_menu_peixe = False
abrir_menu_cao = False

#variaveis de pontos dos boss
pontos_passaro = 0
pontos_peixe = 0
pontos_cao = 0

#derrota e vitoria do jogo
derrota = False
vitoria = False

#mensagem pega chave que aparece na barra de controle
ir_pega_chave_passaro = False
ir_pega_chave_peixe = False


# CARREGAMENTO DAS IMAGENS
#menu principal
menu = pygame.image.load('imagens/menu.jpg')
menu = menu.convert()
menu = pygame.transform.scale(menu, (1000, 700))

#menu de dificuldade
menu_dificuldade = pygame.image.load('imagens/menu_dificuldade.jpg')
menu_dificuldade = menu_dificuldade.convert()
menu_dificuldade = pygame.transform.scale(menu_dificuldade, (1000, 700))

#black (sem fundo)
#black = pygame.image.load('imagens/black_v2_sem_fundo.png')
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

#TELAS (derrota, vitoria, chaves, pontuação)
#tela de derrota (jogo)
tela_de_derrota = pygame.image.load('imagens/tela_de_derrota.jpg')
tela_de_derrota.convert()
tela_de_derrota = pygame.transform.scale(tela_de_derrota, (1000, 700))

#tela de vitoria (jogo)
tela_de_vitoria = pygame.image.load('imagens/tela_de_vitoria.jpg')
tela_de_vitoria.convert()
tela_de_vitoria = pygame.transform.scale(tela_de_vitoria, (1000, 700))

#tela de pontuação
tela_pontuacao = pygame.image.load('imagens/tela_pontuacao.jpg')
tela_pontuacao.convert()
tela_pontuacao = pygame.transform.scale(tela_pontuacao, (1000, 700))

#tela de derrota (chaves)
tela_game_over = pygame.image.load('imagens/tela_game_over.jpg')
tela_game_over.convert()
tela_game_over = pygame.transform.scale(tela_game_over, (1000, 700))

#tela de chaves
tela_de_chaves = pygame.image.load('imagens/tela_de_chaves.jpg')
tela_de_chaves.convert()
tela_de_chaves = pygame.transform.scale(tela_de_chaves, (1000, 700))
#
#mouse (sem fundo)
mouse = pygame.image.load('imagens/mouse_sem_fundo.png')
mouse = mouse.convert_alpha()
mouse = pygame.transform.scale(mouse, (52,35))

#ITENS (com fundo)
#leite
leite = pygame.image.load('imagens/iten_leite.png')
leite = leite.convert()
leite = pygame.transform.scale(leite, (108,111.5))

#sardinha
sardinha = pygame.image.load('imagens/iten_sardinha.png')
sardinha = sardinha.convert()
sardinha = pygame.transform.scale(sardinha, (130, 117.5))

#biscoito de peixe
biscoito_de_peixe = pygame.image.load('imagens/iten_peixe.png')
biscoito_de_peixe = biscoito_de_peixe.convert()
biscoito_de_peixe = pygame.transform.scale(biscoito_de_peixe, (130, 90.5))

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

#MENUS DE BATALHA
#menu de batalha passaro
menu_de_batalha_passaro = pygame.image.load('imagens/menu_de_batalha_passaro.jpg')
menu_de_batalha_passaro = menu_de_batalha_passaro.convert()
menu_de_batalha_passaro = pygame.transform.scale(menu_de_batalha_passaro, (1000, 700))

#menu de batalha peixe
menu_de_batalha_peixe = pygame.image.load('imagens/menu_de_batalha_peixe.jpg')
menu_de_batalha_peixe = menu_de_batalha_peixe.convert()
menu_de_batalha_peixe = pygame.transform.scale(menu_de_batalha_peixe, (1000, 700))

#menu de batalha cao
menu_de_batalha_cao = pygame.image.load('imagens/menu_de_batalha_cao.jpg')
menu_de_batalha_cao = menu_de_batalha_cao.convert()
menu_de_batalha_cao = pygame.transform.scale(menu_de_batalha_cao, (1000, 700))


#BARRA DE TAREFAS
tarefa = 1
#título
font = pygame.font.Font(None, 30) #definir fonte
titulo = font.render(f"OBJETIVO:", True, 'black')
#tarefa 1
font = pygame.font.Font(None, 22) #definir fonte
tarefa1 = font.render(f"* Ir para a casa azul ao oeste", True, 'black')
tarefa1_1 = font.render(f"(talvez consiga alguma informação)", True, 'red')
#tarefa 2
font = pygame.font.Font(None, 22) #definir fonte
tarefa2 = font.render(f"* Ir para a casa de pássaro ao norte", True, 'black')
#tarefa 3
font = pygame.font.Font(None, 22) #definir fonte
tarefa3 = font.render(f"* Ir para o lago ao leste da ilha", True, 'black')
#tarefa 4
font = pygame.font.Font(None, 22) #definir fonte
tarefa4 = font.render(f"* Ir para a casa do cão ao norte", True, 'black')
tarefa4_1 = font.render(f"(É hora da batalha final)", True, 'red')
#caso o player recurse a batalha (orientar ir pega a chave)
font = pygame.font.Font(None, 22) #definir fonte
pega_chave = font.render(f"(conseguir a chave)", True, 'red')

#DIÁLOGOS:
#texto inicial:
font = pygame.font.Font(None, 30) 
texto_inicial = font.render(f"Parece que não foi uma boa ideia pescar durante uma tempestade.", True, 'black')
texto_inicial1 = font.render(f"Você naufragou em uma ilha desconhecida...", True, 'black')
texto_inicial2 = font.render(f"Ela parece meio abandonada.", True, 'black')
texto_inicial3 = font.render(f"Você percebe que algo importante não está mais com você.", True, 'black')
#dialogo_loja
font = pygame.font.Font(None, 30) 
dialogo_loja = font.render(f"Pegue tudo que precisa, mas lembre-se que o dinheiro é finito.", True, 'black')
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
dialogo_passaro9 = font.render(f"Eu tenho uma das chaves e o peixe no lago tem a outra.", True, 'black')
dialogo_passaro10 = font.render(f"Mas não pense que vou dar a minha de graça.", True, 'black')
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
#pular diálogo
pular_dialogo = font.render(f"Pular: p ", True, 'black')
#passar dialogo
passar_dialogo = font.render(f"Próximo: espaço ", True, 'black')
#voltar ao mapa
voltar_ao_mapa = font.render(f"Voltar ao mapa: w", True, 'black')
#ao conseguir a chave
texto_chaves1 = font.render("Você conseguiu a chave!", True, 'black')
texto_chaves2 = font.render("Voltar ao mapa: w", True, 'black')
#tela de pontuação
font_p = pygame.font.Font(None, 35) 
texto_pontuaçao = font_p.render("Sair: y", True, 'white')

#QUADRADOS DAS CASAS
quadrado = pygame.Surface([30, 30]) # cria quadrado com 30 pixels de lado
quadrado_0= pygame.Rect(141, 283, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_1 = pygame.Rect(105, 20, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_2 =pygame.Rect(850, 456, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_3 = pygame.Rect(603,120, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_4 = pygame.Rect(512,350, 30, 30) # cria quadrado com 30 pixels de lado

#QUADRADOS DE FUNDO
#quadrado branco de fundo de diálogo
quadrado_dialogo = pygame.Surface([1000, 40])
quadrado_dialogo.fill((225, 225, 225))
#quadrado branco de fundo dos status
quadrado_status = pygame.Surface([250, 100])
quadrado_status.fill((225, 225, 225))
#quadrado branco de fundo para a barra de tarefas
quadrado_tarefas = pygame.Surface([850, 100])
quadrado_tarefas.fill((225, 225, 225))
#quadrado branco de fundo para mostrar a dificuldade no menu de dificuldade
quadrado_dificuldade = pygame.Surface([300, 40])
quadrado_dificuldade.fill((225, 225, 225))
#quadrado branco de fundo da tela de chaves
quadrado_chaves = pygame.Surface([900, 90])
quadrado_chaves.fill((225, 225, 225))
#quadrado preto da tela de pontuação
quadrado_pontuacao = pygame.Surface([200, 50])
quadrado_pontuacao.fill((0, 0, 0))
#quadrado preto da tela de game over (passaro e peixe)
quadrado_game_over = pygame.Surface([300, 90])
quadrado_game_over.fill((0, 0, 0))

#FUNÇÕES:
#função para o reset do mapa e das telas
def reset_telas():
    global tela_dificuldade, tela_sena_inicial, tela_mapa, tela_dialogo, tela_loja
    global abrir_tela_de_chaves, abrir_tela_de_derrota, abrir_tela_de_vitoria
    global abrir_tela_game_over, abrir_tela_pontuacao
    global tela_dialogo_passaro, tela_dialogo_peixe, tela_dialogo_cao
    global abrir_menu_passaro, abrir_menu_peixe, abrir_menu_cao
    global passar, pular, sim, nao, tempo, nota
    global passaro_luta, peixe_luta

    tela_dificuldade = False
    tela_sena_inicial = False
    tela_mapa = False
    tela_dialogo = False
    tela_dialogo_passaro = False
    tela_dialogo_peixe = False
    tela_dialogo_cao = False
    tela_loja = False

    abrir_menu_passaro = False
    abrir_menu_peixe = False
    abrir_menu_cao = False

    abrir_tela_de_chaves = False
    abrir_tela_de_derrota = False
    abrir_tela_de_vitoria = False
    abrir_tela_game_over = False
    abrir_tela_pontuacao = False

    tempo = 0
    passar = 0
    pular = 0
    sim = 0
    nao = 0

def reset_status():
    global chaves, vidas, dinheiro, tarefa, nota

    chaves = 0
    vidas = 1
    dinheiro = 300
    tarefa = 1
    nota = 0

while True:
    for event in pygame.event.get():
        #FECHAR O JOGO:
        if event.type == pygame.QUIT: #clicar no x
            pygame.quit()
            exit()

        #POSIÇÃO DO MOUSE
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        
        #EVENTOS DAS TECLAS
        if event.type == pygame.KEYDOWN:
            #SAIR DO JOGO QUANDO PERDER
            if abrir_tela_de_derrota == True: #só se já tiver perdido o jogo
                if event.key == pygame.K_b: #tecla B
                    pygame.quit()
                    exit()

            #VOLTAR PARA A CENA INICIAL
            if abrir_tela_de_derrota == True: #só se já tiver perdido o jogo
                if event.key == pygame.K_e: #tecla E
                    reset_telas()
                    reset_status()
                    tela_sena_inicial = True

            #ABRIR MENU DE DIFICULDADES
            if event.key == pygame.K_RETURN: #tecla ENTER
                reset_telas()
                tela_dificuldade = True

            #OPÇÕES DO MENU DE DIFICULDADES
            if event.key == pygame.K_f: #tecla F (fácil)
                dificuldade = "fácil"
            if event.key == pygame.K_m: #tecla M (médio)
                dificuldade = "médio"
            if event.key == pygame.K_d: #tecla D (díficil)
                dificuldade = "difícil"
            if event.key == pygame.K_a:
                reset_telas()
                tela_sena_inicial = True
                

            #ABRIR MAPA
            if event.key == pygame.K_w:
                reset_telas()
                tela_mapa = True
                print("Mapa aberto")

            #PASSAGEM DE DIÁLOGO
            if event.key == pygame.K_SPACE:
                passar += 1 #passar diálogo
            if event.key == pygame.K_p: #seta para cima
                pular += 1 #pular diálogo

            #ACEITAR OU RECUSAR BATALHA
            if event.key == pygame.K_s:
                sim = sim + 1
            if event.key == pygame.K_n:
                nao = nao + 1

            #SAIR DA TELA DE PONTUAÇÃO
            if event.key == pygame.K_y and abrir_tela_pontuacao == True:
                abrir_tela_pontuacao = False

                #passaro
                if nota_passaro == "A" and nota == 1:
                    abrir_tela_de_chaves = True
                    tarefa += 1
                    chaves += 1
                elif nota_passaro == "F" and nota == 1:
                    abrir_tela_game_over = True
                    if vidas == 1:
                        abrir_tela_de_derrota = True
                    elif vidas == 2:
                        tela_mapa = True
                        vidas -= 1

                #peixe
                if nota_peixe == "A" and nota == 2:
                    abrir_tela_de_chaves = True
                    tarefa += 1
                    chaves += 1
                elif nota_peixe == "F" and nota == 2:
                    abrir_tela_game_over = True
                    if vidas == 1:
                        abrir_tela_de_derrota = True
                    elif vidas == 2:
                        tela_mapa = True
                        vidas -= 1

                #cao
                if nota_cao == "A" and nota == 3:
                    abrir_tela_de_vitoria = True
                elif nota_cao == "F" and nota == 3:
                    abrir_tela_game_over = True
                    if vidas == 1:
                        abrir_tela_de_derrota = True
                    elif vidas == 2:
                        tela_mapa == True
                        vidas -= 1



            #DEPOIS DE PERDER UMA BATALHA (passaro ou peixe)
            if event.key == pygame.K_z:
                if abrir_tela_game_over == True:
                    if vidas == 0:
                        reset_telas()
                        abrir_tela_de_derrota = True
                    elif vidas == 1:
                        tela_mapa = True

        #CONTROLE DO SENSOR DE CLIQUE NOS QUADRADOS DAS CASAS
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and tela_mapa:
                if quadrado_0.collidepoint(event.pos):
                    if tarefa == 1:
                        reset_telas()
                        tela_dialogo = True          
                elif quadrado_1.collidepoint(event.pos):
                    if tarefa == 2: #só vai conseguir entrar no quadrado se for a tarefa certa
                        reset_telas()
                        tela_dialogo_passaro = True
                elif quadrado_2.collidepoint(event.pos):
                    if tarefa == 3: #só vai conseguir entrar no quadrado se for a tarefa certa
                        reset_telas()
                        tela_dialogo_peixe = True
                elif quadrado_3.collidepoint(event.pos):
                    if tarefa == 4 and chaves == 2: #só vai conseguir entrar no quadrado se for a tarefa certa e também se tiver as 2 chaves
                        reset_telas()
                        tela_dialogo_cao = True
                elif quadrado_4.collidepoint(event.pos):
                    reset_telas()
                    tela_loja = True
                elif quadrado_1.collidepoint(event.pos):
                    reset_telas()
                    tela_boss_1 = True
                elif quadrado_2.collidepoint(event.pos):
                    reset_telas()
                    tela_boss_2 = True
                elif quadrado_3.collidepoint(event.pos):
                    reset_telas()
                    tela_boss_3 = True
                elif quadrado_4.collidepoint(event.pos):
                    reset_telas()
                    tela_loja = True

    janela.fill((255, 255, 255))

    # TELAS ESPECIAIS 
    #tela de pontuação
    if abrir_tela_pontuacao:
        janela.blit(tela_pontuacao, (0, 0))
        janela.blit(quadrado_pontuacao, (800, 630))
        janela.blit(texto_pontuaçao, (850, 640))
        #CALCULAR OS PONTOS DOS BOSS PELA DIFICULDADE
        if dificuldade == "fácil":
            pontos_passaro = 10
            pontos_peixe = 20
            pontos_cao = 30
        elif dificuldade == "médio":
            pontos_passaro = 20
            pontos_peixe = 30
            pontos_cao = 40
        elif dificuldade == "difícil":
            pontos_passaro = 30
            pontos_peixe = 40
            pontos_cao = 50

        ##INFORMAÇÕES:
        font_pontuacao = pygame.font.Font(None, 45) 
        interrogacao = font_pontuacao.render(f"?", True, 'black')
        #black x passaro
        informacao_pontuacao_black1 = font_pontuacao.render(f"{pontos_black1}", True, 'red')
        informacao_pontuacao_passaro = font_pontuacao.render(f"{pontos_passaro}", True, 'black')
        if chaves >= 0: #passaro
            janela.blit(informacao_pontuacao_black1, (790, 255))
            janela.blit(informacao_pontuacao_passaro, (790, 285))
        else:
            janela.blit(interrogacao, (790, 255))
            janela.blit(interrogacao, (790, 285))


        #black x peixe
        informacao_pontuacao_black2 = font_pontuacao.render(f"{pontos_black2}", True, 'red')
        informacao_pontuacao_peixe = font_pontuacao.render(f"{pontos_peixe}", True, 'black')
        if chaves >= 1: #peixe
            janela.blit(informacao_pontuacao_black2, (790, 348))
            janela.blit(informacao_pontuacao_peixe, (790, 375))
        else:
            janela.blit(interrogacao, (790, 348))
            janela.blit(interrogacao, (790, 375))

        #black x cao
        informacao_pontuacao_black3 = font_pontuacao.render(f"{pontos_black3}", True, 'red')
        informacao_pontuacao_cao = font_pontuacao.render(f"{pontos_cao}", True, 'black')
        if chaves == 2:
            janela.blit(informacao_pontuacao_black3, (790, 434))
            janela.blit(informacao_pontuacao_cao, (790, 464))
        else:
            janela.blit(interrogacao, (790, 434))
            janela.blit(interrogacao, (790, 464))

        #NOTA
        #comparar prontos do black com o do boss
        #passaro
        if pontos_black1 >= pontos_passaro and nota == 1: #o jogador fizer mais pontos ou igual que o boss tem
            nota_passaro = "A"
        elif nota == 1:
            nota_passaro = "F"
            ir_pega_chave_passaro = True

        #peixe
        if pontos_black2 >= pontos_peixe and nota == 2: #o jogador fizer mais pontos ou igual que o boss tem
            nota_peixe = "A"
        elif nota == 2:
            nota_peixe = "F"
            ir_pega_chave_peixe = True

        #cao
        if pontos_black3 >= pontos_cao and nota == 3: #o jogador fizer mais pontos ou igual que o boss tem
            nota_cao = "A"
        elif nota == 3:
            nota_cao = "F"
        #

        font_nota = pygame.font.Font(None, 100) 
        if nota == 1: #passaro
            if nota_passaro == "A":
                informacao_nota = font_nota.render(f"{nota_passaro}", True, 'blue')
                janela.blit(informacao_nota, (720, 500))
            elif nota_passaro == "F":
                informacao_nota = font_nota.render(f"{nota_passaro}", True, 'red')
                janela.blit(informacao_nota, (720, 500))

        if nota == 2: #peixe
            if nota_peixe == "A":
                informacao_nota = font_nota.render(f"{nota_peixe}", True, 'blue')
                janela.blit(informacao_nota, (720, 500))
            elif nota_peixe == "F":
                informacao_nota = font_nota.render(f"{nota_peixe}", True, 'red')
                janela.blit(informacao_nota, (720, 500))

        if nota == 3: #cao
            if nota_cao == "A":
                informacao_nota = font_nota.render(f"{nota_cao}", True, 'blue')
                janela.blit(informacao_nota, (720, 500))
            elif nota_cao == "F":
                informacao_nota = font_nota.render(f"{nota_cao}", True, 'red')
                janela.blit(informacao_nota, (720, 500))


    #tela de chaves
    elif abrir_tela_de_chaves:
        janela.blit(tela_de_chaves, (0, 0))
        janela.blit(quadrado_chaves, (770, 20))
        janela.blit(texto_chaves1, (790, 40))
        janela.blit(texto_chaves2, (790, 60))

    #tela de game over
    elif abrir_tela_game_over:
        janela.blit(tela_game_over, (0, 0))
        janela.blit(quadrado_game_over, (0, 600))
        #texto
        texto_game_over1 = font.render("Você foi derrotado..", True, 'white')
        texto_game_over2 = font.render(f"Vidas restantes: {vidas}", True, 'white')
        janela.blit(texto_game_over1, (60, 630))
        janela.blit(texto_game_over2, (60, 650))

    #tela de derrota
    elif abrir_tela_de_derrota:
        janela.blit(tela_de_derrota, (0, 0))

    #tela de vitoria
    elif abrir_tela_de_vitoria:
        janela.blit(tela_de_vitoria, (0, 0))

    # MENU 
    elif tela_dificuldade or not tela_sena_inicial:
        janela.blit(menu, (0, 0))

    #MENU DE DIFICULDADE
    if tela_dificuldade:
        janela.blit(menu_dificuldade, (0, 0)) #imagem de fundo
        janela.blit(quadrado_dificuldade, (0, 638))
        #dificuldade seleciona no menu de dificuldade
        dificuldade_escolhida = font.render(f"Dificuldade: {dificuldade}", True, 'black')
        janela.blit(dificuldade_escolhida, (100, 650)) 

    #CENA INICIAL
    if tela_sena_inicial:
        janela.blit(sena_inicial, (0, 0)) #imagem de fundo
        janela.blit(texto_inicial, (200, 610)) #texto
        janela.blit(texto_inicial1, (200, 630))
        janela.blit(texto_inicial2, (200, 650))
        janela.blit(texto_inicial3, (200, 670))

    #MAPA
    if tela_mapa:
        janela.blit(mapa, (0, 0))
        janela.blit(rosa, (850, 10))
        janela.blit(quadrado_status, (0, 580)) #quadrado de fundo dos status

        #STATUS: (dinheiro, chaves, vidas e dificuldade atual do jogo)
        #status de dinheiro:
        font = pygame.font.Font(None, 30) #definir fonte
        status_dinheiro = font.render(f"Dinheiro: R${dinheiro}", True, 'black')
        #quantidade de chaves:
        font = pygame.font.Font(None, 30) #definir fonte
        status_chaves = font.render(f"Chaves: {chaves}/2", True, 'black')
        #quantidade de vidas restantes
        font = pygame.font.Font(None, 30) #definir fonte
        status_vidas = font.render(f"Vidas restantes: {vidas}", True, 'black')
        #nível de dificuldade
        font = pygame.font.Font(None, 30) #definir fonte
        status_dificuldade = font.render(f"Dificuldade: {dificuldade}", True, 'black')
                
        janela.blit(status_dinheiro, (10, 650))
        janela.blit(status_chaves, (10, 630))
        janela.blit(status_vidas, (10, 610))
        janela.blit(status_dificuldade, (10, 590))
        janela.blit(quadrado_tarefas, (700, 130)) #quadrado de fundo das tarefas

        janela.blit(titulo, (725, 140))
        if tarefa == 1:
            janela.blit(tarefa1, (740, 170))
            janela.blit(tarefa1_1, (740, 190))
        elif tarefa == 2:
            janela.blit(tarefa2, (740, 170))
            if ir_pega_chave_passaro == True:
                janela.blit(pega_chave, (740, 190)) #colocar uma pequena mensagem mandando pegar a chave
        elif tarefa == 3:
            janela.blit(tarefa3, (740, 170))
            if ir_pega_chave_peixe == True:
                janela.blit(pega_chave, (740, 190)) #colocar uma pequena mensagem mandando pegar a chave
        elif tarefa == 4:
            janela.blit(tarefa4, (740, 170))
            janela.blit(tarefa4_1, (740, 190))

        quadrado.fill((225, 0, 0))
        janela.blit(quadrado, quadrado_0)
        janela.blit(quadrado, quadrado_1)
        janela.blit(quadrado, quadrado_2)
        janela.blit(quadrado, quadrado_3)
        janela.blit(quadrado, quadrado_4)

        janela.blit(black, (mouse_x, mouse_y))


    #DIALOGO GATO
    if tela_dialogo:
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(dialogo_1, (0, 0))
        janela.blit(pular_dialogo, (800, 60))
        janela.blit(passar_dialogo, (800, 40))
        janela.blit(voltar_ao_mapa, (800, 20))

        quadrado_dialogo = pygame.Surface((1000, 40))
        quadrado_dialogo.fill((225, 225, 225))
        janela.blit(quadrado_dialogo, (0, 638))

        textos = [
            primeiro_dialogo1, primeiro_dialogo2, primeiro_dialogo3,
            primeiro_dialogo4, primeiro_dialogo5, primeiro_dialogo6,
            primeiro_dialogo7, primeiro_dialogo8, primeiro_dialogo9,
            primeiro_dialogo10, primeiro_dialogo11
        ]
        
        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado
            tarefa = 2
            tela_mapa = True #voltar ao mapa assim que acabar o diálogo
            tela_dialogo = False
    
    #DIALOGO PASSARO
    if tela_dialogo_passaro:
        janela.blit(passaro, (0, 0))
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(pular_dialogo, (800, 60)) #orientação
        janela.blit(passar_dialogo, (800, 40)) #orientação
        janela.blit(voltar_ao_mapa, (800, 20)) #orientação

        textos = [
            dialogo_passaro1, dialogo_passaro2, dialogo_passaro3,
            dialogo_passaro4, dialogo_passaro5, dialogo_passaro6,
            dialogo_passaro7, dialogo_passaro8, dialogo_passaro9,
            dialogo_passaro10, dialogo_passaro11, dialogo_passaro12,
            dialogo_passaro13
        ]

        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado vai direto pro menu
            abrir_menu_passaro = True
            tela_dialogo_passaro = False
        
    #BATALHA PÁSSARO
    if abrir_menu_passaro:
        janela.blit(menu_de_batalha_passaro, (0, 0))

        if sim == 1:
            nota += 1
            abrir_menu_passaro = False
            sim = 0
            nao = 0

            if pontos_black1 >= pontos_passaro:
                nota_passaro = "A"
            else:
                nota_passaro = "F"
                ir_pega_chave_passaro = True
                vidas -= 1

            abrir_tela_pontuacao = True

        elif nao == 1:
            abrir_menu_passaro = False
            sim = 0
            nao = 0
            tela_mapa = True

    #DIALOGO PEIXE
    if tela_dialogo_peixe:
        janela.blit(peixe, (0, 0))
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(pular_dialogo, (800, 60)) #orientação
        janela.blit(passar_dialogo, (800, 40))
        janela.blit(voltar_ao_mapa, (800, 20))

        textos = [
            dialogo_peixe1, dialogo_peixe2, dialogo_peixe3,
            dialogo_peixe4, dialogo_peixe5, dialogo_peixe6,
            dialogo_peixe7, dialogo_peixe8, dialogo_peixe9,
            dialogo_peixe10, dialogo_peixe11
        ]

        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado vai direto pro menu
            abrir_menu_peixe = True
            tela_dialogo_peixe = False

    #BATALHA PEIXE
    if abrir_menu_peixe:
        janela.blit(menu_de_batalha_peixe, (0, 0))

        if sim == 1:
            nota += 1
            abrir_menu_peixe = False
            sim = 0
            nao = 0

            if pontos_black2 >= pontos_peixe:
                nota_peixe = "A"
            else:
                nota_peixe = "F"
                ir_pega_chave_peixe = True
                vidas -= 1

            abrir_tela_pontuacao = True

        elif nao == 1:
            abrir_menu_peixe = False
            sim = 0
            nao = 0
            tela_mapa = True
    #DIALOGO CAO
    if tela_dialogo_cao:
        janela.blit(cao, (0, 0))
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(pular_dialogo, (800, 60)) #orientação
        janela.blit(passar_dialogo, (800, 40))
        janela.blit(voltar_ao_mapa, (800, 20))

        textos = [
            dialogo_cao1, dialogo_cao2, dialogo_cao3, dialogo_cao4,
            dialogo_cao5, dialogo_cao6, dialogo_cao7, dialogo_cao8,
            dialogo_cao9, dialogo_cao10, dialogo_cao11, dialogo_cao12,
            dialogo_cao13, dialogo_cao14, dialogo_cao15, dialogo_cao16
        ]

        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado vai direto pro menu
            abrir_menu_cao = True
            tela_dialogo_cao = False

    #BATALHA CÃO
    if abrir_menu_cao:
        janela.blit(menu_de_batalha_cao, (0, 0))

        if sim == 1:
            nota += 1
            abrir_menu_cao = False
            sim = 0
            nao = 0

            if pontos_black3 >= pontos_cao:
                nota_cao = "A"
                abrir_tela_de_vitoria = True
            else:
                nota_cao = "F"
                vidas -= 1
                abrir_tela_de_derrota = True

            abrir_tela_pontuacao = True
    #LOJA
    if tela_loja:
        janela.blit(loja, (0, 0))

        #texto
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de fundo de dialogo
        janela.blit(quadrado_status, (0, 530)) #quadrado branco de fundo dos status
        janela.blit(dialogo_loja, (200, 650))
        janela.blit(voltar_ao_mapa, (800, 20))

        #status
        #(10, 540)
        #(10, 560)
        #(10, 580)
        #(10, 600)
        janela.blit(status_dinheiro, (10, 540)) #-20 pixel
        janela.blit(status_chaves, (10, 560))
        janela.blit(status_vidas, (10, 580))
        janela.blit(status_dificuldade, (10, 600))

        #itens
        janela.blit(biscoito_de_peixe, (100, 250))
        janela.blit(sardinha, (300, 250))
        janela.blit(leite, (500, 250))

    pygame.display.flip()
    clock.tick(60)