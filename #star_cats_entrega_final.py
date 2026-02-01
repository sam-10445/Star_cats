import pygame
import sys, random
import pygame as pg
pygame.init()
pygame.display.set_caption("Star Cats")
janela = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

#MECANICA DE BATALHA (sprite)
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

#controle do botão de enter
passou_do_menu_dificuldade = False

#telas especiais
abrir_tela_de_chaves = False
abrir_tela_de_derrota = False
abrir_tela_de_vitoria = False
abrir_tela_pontuacao = False
abrir_tela_game_over = False

abrir_tela_creditos = False

#controle de passagem de diálogos
passar = 0
pular = 0

#variáveis de status (iniciais)
dificuldade = "fácil"
chaves = 0
vidas = 1
dinheiro = 300

#variaveis de quantidade dos itens (inicial)
n_biscoito_peixe = 0
n_sardinha = 0
n_leite = 0 #acaba que quando você entra na loja automaticamente compra um leite

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
#ativação das batalhas
abrir_batalha_passaro = False
abrir_batalha_peixe = False
abrir_batalha_cao = False

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

#TEMPORIZADOR DAS BATALHAS
bonus_tempo = 0
em_batalha_passaro = False
em_batalha_peixe = False
em_batalha_cao = False
inicio_batalha = 0
TEMPO_BASE_BATALHA = 10
DURACAO_BATALHA = TEMPO_BASE_BATALHA
inicio_batalha = pygame.time.get_ticks()
batalha_ativa = True

#MINI-GAME DAS BATALHAS
GRID_LINHAS = 4
GRID_COLUNAS = 4
TAM_QUADRADO = 90
GRID_X = 550
GRID_Y = 180

quadrados_mini_game = []
indice_ativo = -1
tipo_ativo = None  
tempo_quadrado = 0
TEMPO_QUADRADO = 800  

mini_game_iniciado = False

#
for linha in range(GRID_LINHAS):
    for coluna in range(GRID_COLUNAS):
        ESPACO = 8
        x = GRID_X + coluna * (TAM_QUADRADO + ESPACO)
        y = GRID_Y + linha * (TAM_QUADRADO + ESPACO)
        quadrados_mini_game.append(
            pygame.Rect(x, y, TAM_QUADRADO, TAM_QUADRADO)
        )




# CARREGAMENTO DAS IMAGENS
#tela de créditos
tela_creditos = pygame.image.load('imagens/tela_creditos.jpg')
tela_creditos = tela_creditos.convert()
tela_creditos = pygame.transform.scale(tela_creditos, (1000, 700))

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

#PASSARO
#diálogo
passaro = pygame.image.load('imagens/passaro.jpg')
passaro = passaro.convert()
passaro = pygame.transform.scale(passaro, (1000, 700))
#batalha
passaro_batalha = pygame.image.load('imagens/passaro_batalha.jpg')
passaro_batalha = passaro_batalha.convert()
passaro_batalha = pygame.transform.scale(passaro_batalha, (1000, 700))

#PEIXE
#diálogo
peixe = pygame.image.load('imagens/peixe.jpg')
peixe = peixe.convert()
peixe = pygame.transform.scale(peixe, (1000, 700))
#batalha
peixe_batalha = pygame.image.load('imagens/peixe_batalha.png')
peixe_batalha = peixe_batalha.convert()
peixe_batalha = pygame.transform.scale(peixe_batalha, (1000, 700))

#CÃO
#diálogo
cao = pygame.image.load('imagens/cao.jpg')
cao = cao.convert()
cao = pygame.transform.scale(cao, (1000, 700))
#batalha
cao_batalha = pygame.image.load('imagens/cao_batalha.jpg')
cao_batalha = cao_batalha.convert()
cao_batalha = pygame.transform.scale(cao_batalha, (1000, 700))

#loja
loja = pygame.image.load('imagens/loja.jpg')
loja = loja.convert()
loja = pygame.transform.scale(loja, (1000, 700))

#TELAS (derrota, vitoria, chaves, pontuação)
#tela de derrota (jogo)
tela_de_derrota = pygame.image.load('imagens/tela_de_derrota.jpg')
tela_de_derrota = tela_de_derrota.convert()
tela_de_derrota = pygame.transform.scale(tela_de_derrota, (1000, 700))

#tela de vitoria (jogo)
tela_de_vitoria = pygame.image.load('imagens/tela_de_vitoria.jpg')
tela_de_vitoria = tela_de_vitoria.convert()
tela_de_vitoria = pygame.transform.scale(tela_de_vitoria, (1000, 700))

#tela de pontuação
tela_pontuacao = pygame.image.load('imagens/tela_pontuacao.jpg')
tela_pontuacao = tela_pontuacao.convert()
tela_pontuacao = pygame.transform.scale(tela_pontuacao, (1000, 700))

#tela de derrota (chaves)
tela_game_over = pygame.image.load('imagens/tela_game_over.jpg')
tela_game_over = tela_game_over.convert()
tela_game_over = pygame.transform.scale(tela_game_over, (1000, 700))

#tela de chaves
tela_de_chaves = pygame.image.load('imagens/tela_de_chaves.jpg')
tela_de_chaves = tela_de_chaves.convert()
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
tarefa1_1 = font.render(f"(buscar por informações)", True, 'red')
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
texto_inicial1 = font.render(f"Seu barco virou e agora você está em uma ilha desconhecida.", True, 'black')
texto_inicial2 = font.render(f"Ela parece meio abandonada - você pensa.", True, 'black')
texto_inicial3 = font.render(f"Quando percebe que algo importante não está mais com você.", True, 'black')
#dialogo_loja
font = pygame.font.Font(None, 30) 
dialogo_loja1 = font.render(f"Clique nos itens que deseja comprar.", True, 'white')
dialogo_loja2 = font.render(f"Mas use o dinheiro com sabedoria.", True, 'white')

#PRIMEIRO DIÁLOGO:
font = pygame.font.Font(None, 30) 
primeiro_dialogo1 = font.render(f"Olá, pequeno visitante!", True, 'black')
primeiro_dialogo2 = font.render(f"O que aconteceu? Você parece perdido.", True, 'black')
#pergunta obrigatoria: Meu barco virou.
pergunta1_gato = font.render(f"  Meu barco virou.", True, 'white')
#
primeiro_dialogo3 = font.render(f"...", True, 'black')
primeiro_dialogo4 = font.render(f"Ah… sinto muito.", True, 'black')
#pergunta obrigatoria: Estou procurando por uma estrela. 
pergunta2_gato = font.render(f" Estou procurando por uma estrela.", True, 'white')
#
primeiro_dialogo5 = font.render(f"...", True, 'black')
primeiro_dialogo6 = font.render(f"Uma estrela?! …", True, 'black')
primeiro_dialogo7 = font.render(f"Isso não é algo comum de se perder.", True, 'black')
primeiro_dialogo8 = font.render(f"Bom… não sei onde ela está,", True, 'black')
primeiro_dialogo9 = font.render(f"mas talvez eu tenha um palpite.", True, 'black')
primeiro_dialogo10 = font.render(f"Ao norte da ilha vive um cão.", True, 'black')
primeiro_dialogo11 = font.render(f"Ele costuma juntar tudo o que considera valioso.", True, 'black')
primeiro_dialogo12 = font.render(f"Se sua estrela existe,", True, 'black')
primeiro_dialogo13 = font.render(f"e se ele a encontrou,", True, 'black')
primeiro_dialogo14 = font.render(f"é bem provável que esteja com ele agora.", True, 'black')
primeiro_dialogo15 = font.render(f"O problema é chegar até lá.", True, 'black')
primeiro_dialogo16 = font.render(f"O lugar é trancado por dois cadeados,", True, 'black')
primeiro_dialogo17 = font.render(f"e eu não tenho as chaves.", True, 'black')
primeiro_dialogo18 = font.render(f"Talvez o pássaro ao norte consiga te ajudar.", True, 'black')
primeiro_dialogo19 = font.render(f"Que tal ir falar com ele depois?", True, 'black')
primeiro_dialogo20 = font.render(f"Sinto muito por não poder fazer mais.", True, 'black')
primeiro_dialogo21 = font.render(f"Mas… se quiser, pode me fazer algumas perguntas.", True, 'black')
#pergunta obrigatoria: Quem é você?
pergunta3_gato = font.render(f" Quem é você?", True, 'white')
#
primeiro_dialogo22 = font.render(f"...", True, 'black')
primeiro_dialogo23 = font.render(f"Eu sou o administrador desta ilha!", True, 'black')
primeiro_dialogo24 = font.render(f"Ou… pelo menos, era.", True, 'black')
primeiro_dialogo25 = font.render(f"Mais alguma pergunta?", True, 'black')
#pergunta obrigatoria: O que aconteceu com a ilha?
pergunta4_gato = font.render(f" O que aconteceu com a ilha?", True, 'white')
#
primeiro_dialogo26 = font.render(f"...", True, 'black')
primeiro_dialogo27 = font.render(f"…É uma longa história,", True, 'black')
primeiro_dialogo28 = font.render(f"mas vou tentar resumir.", True, 'black')
primeiro_dialogo29  = font.render(f"No começo, éramos só nós três:", True, 'black')
primeiro_dialogo30 = font.render(f"eu, o pássaro e o peixe.", True, 'black')
primeiro_dialogo31 = font.render(f"Vivíamos bem assim.", True, 'black')
primeiro_dialogo32 = font.render(f"Mas quando aquele canino chegou,", True, 'black')
primeiro_dialogo33 = font.render(f"as coisas... mudaram.", True, 'black')
primeiro_dialogo34 = font.render(f"Ele começou a recolher tudo o que encontrava.", True, 'black')
primeiro_dialogo35 = font.render(f"Sendo dele… ou não.", True, 'black')
primeiro_dialogo36 = font.render(f"Algumas dessas coisas eram importantes para nós.", True, 'black')
primeiro_dialogo37 = font.render(f"Ele era mais forte,", True, 'black')
primeiro_dialogo38 = font.render(f"então não conseguimos impedi-lo.", True, 'black')
primeiro_dialogo39 = font.render(f"Hoje, ele controla quem entra e quem sai da ilha.", True, 'black')
primeiro_dialogo40 = font.render(f"As únicas visitas que recebemos agora são…", True, 'black')
primeiro_dialogo41 = font.render(f"os comerciantes que ele permite entrar…", True, 'black')
primeiro_dialogo42 = font.render(f"E aqueles que acabam parando aqui sem querer.", True, 'black')
primeiro_dialogo43 = font.render(f"Como você.", True, 'black')
primeiro_dialogo44 = font.render(f"Mais alguma pergunta?", True, 'black')
#pergunta obrigatoria: Tem algum jeito de sair da ilha?
pergunta5_gato = font.render(f" Tem algum jeito de sair da ilha?", True, 'white')
#
primeiro_dialogo45 = font.render(f"...", True, 'black')
primeiro_dialogo46 = font.render(f"Mas é claro que tem!", True, 'black')
primeiro_dialogo47 = font.render(f"O difícil mesmo é ficar.", True, 'black')
primeiro_dialogo48 = font.render(f"O cachorro não costuma deixar visitantes por muito tempo.", True, 'black')
primeiro_dialogo49 = font.render(f"Por isso, sempre mantenho um barco reserva.", True, 'black')
primeiro_dialogo50 = font.render(f"Se quiser, posso buscá-lo agora mesmo", True, 'black')
primeiro_dialogo51 = font.render(f"e você pode ir para casa.", True, 'black')
primeiro_dialogo52 = font.render(f"Quer que eu vá buscá-lo?", True, 'black')
#pergunta obrigatoria: Ainda não. Preciso da minha estrela
pergunta6_gato = font.render(f" Ainda não. Preciso da minha estrela", True, 'white')
#
primeiro_dialogo53 = font.render(f"...", True, 'black')
primeiro_dialogo54 = font.render(f"Ah… é mesmo. A estrela.", True, 'black')
primeiro_dialogo55 = font.render(f"Não sei se você vai conseguir recuperá-la,", True, 'black')
primeiro_dialogo56 = font.render(f"mas quando estiver pronto para partir…", True, 'black')
primeiro_dialogo57 = font.render(f"Pode contar comigo para preparar sua passagem de volta.", True, 'black')
primeiro_dialogo58 = font.render(f"Mais alguma pergunta?", True, 'black')
#pergunta obrigatoria: Há algo que possa me ajudar?
pergunta7_gato = font.render(f" Há algo que possa me ajudar?", True, 'white')
#
primeiro_dialogo59 = font.render(f"...", True, 'black')
primeiro_dialogo60 = font.render(f"Uh… deixa eu pensar.", True, 'black')
primeiro_dialogo61 = font.render(f"No centro da ilha há um comerciante", True, 'black')
primeiro_dialogo62  = font.render(f"que eu nunca tinha visto antes.", True, 'black')
primeiro_dialogo63 = font.render(f"Ele vende coisas interessantes.", True, 'black')
primeiro_dialogo64 = font.render(f"Talvez alguma delas possa te ajudar.", True, 'black')
primeiro_dialogo65 = font.render(f"Se estiver curioso,", True, 'black')
primeiro_dialogo66 = font.render(f"dê uma olhada nas mercadorias.", True, 'black')
primeiro_dialogo67 = font.render(f"Mais alguma pergunta?", True, 'black')
#pergunta obrigatoria: Não, obrigado.
pergunta8_gato = font.render(f" Não, obrigado.", True, 'white')
#
primeiro_dialogo68 = font.render(f"...", True, 'black')
primeiro_dialogo69 = font.render(f"Espero ter ajudado.", True, 'black')
primeiro_dialogo70 = font.render(f"Não se esqueça de visitar o pássaro ao norte…", True, 'black')
primeiro_dialogo71 = font.render(f"E a loja no centro da ilha.", True, 'black')
primeiro_dialogo72 = font.render(f"Boa sorte :)", True, 'black')


#DIÁLOGO PASSARO
font = pygame.font.Font(None, 30) 
#pergunta obrigatoria: Você viu uma Estrela? 
pergunta1_passaro = font.render(f"  Você viu uma Estrela?", True, 'white')
#
dialogo_passaro1 = font.render(f"...", True, 'black')
dialogo_passaro2 = font.render(f"Uma estrela?", True, 'black')
dialogo_passaro3 = font.render(f"E desde quando isso é possível?", True, 'black')
dialogo_passaro4 = font.render(f"Olha, gatinho", True, 'black')
dialogo_passaro5 = font.render(f"não vi nenhuma estrela passeando por aí.", True, 'black')
dialogo_passaro6 = font.render(f"E a ilha nem é tão grande assim.", True, 'black')
dialogo_passaro7 = font.render(f"Mas se ela realmente existe…", True, 'black')
dialogo_passaro8 = font.render(f"provavelmente está na casa daquele cachorro.", True, 'black')
dialogo_passaro9 = font.render(f"Ele gosta de guardar tudo o que encontra.", True, 'black')
dialogo_passaro10 = font.render(f"Mesmo quando isso é importante para outra pessoa…", True, 'black')
#pergunta obrigatoria: O que aconteceu? 
pergunta2_passaro = font.render(f"  O que aconteceu?", True, 'white')
#
dialogo_passaro11 = font.render(f"...", True, 'black')
dialogo_passaro12 = font.render(f"Ah… o de sempre!", True, 'black')
dialogo_passaro13 = font.render(f"Ele chega, olha em volta", True, 'black')
dialogo_passaro14 = font.render(f"e decide que aquilo precisa ser “guardado”.", True, 'black')
dialogo_passaro15 = font.render(f"Mesmo quando deu trabalho conseguir.", True, 'black')
dialogo_passaro16 = font.render(f"...", True, 'black')
dialogo_passaro17 = font.render(f"No meu caso…", True, 'black')
dialogo_passaro18 = font.render(f"foram minhas sementes favoritas.", True, 'black')
dialogo_passaro19 = font.render(f"Não eram raras.", True, 'black')
dialogo_passaro20 = font.render(f"Só tinham um gosto especial.", True, 'black')
dialogo_passaro21 = font.render(f"Agora sinto falta delas.", True, 'black')
#pergunta obrigatoria: Você tem a chave de um dos cadeados?
pergunta3_passaro = font.render(f" Você tem a chave de um dos cadeados?", True, 'white')
#
dialogo_passaro22 = font.render(f"...", True, 'black')
dialogo_passaro23 = font.render(f"Cadeado…?", True, 'black')
dialogo_passaro24 = font.render(f"Ah, é. A estrela.", True, 'black')
dialogo_passaro25 = font.render(f"Não me diga que está pensando em ir buscá-la? Haha.", True, 'black')
dialogo_passaro26 = font.render(f"Olha… não acho que seja uma boa ideia.", True, 'black')
dialogo_passaro27 = font.render(f"Mas também não vou te impedir.", True, 'black')
dialogo_passaro28 = font.render(f"Então, sim, eu tenho uma das chaves.", True, 'black')
dialogo_passaro29 = font.render(f"A outra está com o peixe, no lago.", True, 'black')
dialogo_passaro30 = font.render(f"Se você quer mesmo sua estrela de volta,", True, 'black')
dialogo_passaro31 = font.render(f"vai ter que falar com ele também.", True, 'black')
dialogo_passaro32 = font.render(f"Mas não vou entregar a minha chave assim tão fácil!", True, 'black')
dialogo_passaro33 = font.render(f"Que tal uma batalha?", True, 'black')
dialogo_passaro34 = font.render(f"Nada pessoal, só por diversão.", True, 'black')
dialogo_passaro35 = font.render(f"Se vencer, a chave é sua!", True, 'black')
dialogo_passaro36 = font.render(f"Aceita?", True, 'black')

#DIÁLOGO PEIXE
font = pygame.font.Font(None, 30) 
#pergunta obrigatoria: Você viu uma Estrela? 
pergunta1_peixe = font.render(f"  Você viu uma Estrela?", True, 'white')
#
dialogo_peixe1 = font.render(f"...", True, 'black')
dialogo_peixe2 = font.render(f"…Uma estrela?", True, 'black')
dialogo_peixe3 = font.render(f"Não vi nada assim.", True, 'black')
dialogo_peixe4 = font.render(f"Aqui no lago, o céu quase não aparece.", True, 'black')
dialogo_peixe5 = font.render(f"Mas se for algo importante…", True, 'black')
dialogo_peixe6 = font.render(f"imagino que esteja com o cachorro.", True, 'black')
dialogo_peixe7 = font.render(f"Ele pega tudo de todo mundo.", True, 'black')
#pergunta obrigatoria: Ele também pegou algo seu?
pergunta2_peixe = font.render(f"  Ele também pegou algo seu?", True, 'white')
#
dialogo_peixe8 = font.render(f"...", True, 'black')
dialogo_peixe9 = font.render(f"Pegou, sim.", True, 'black')
dialogo_peixe10 = font.render(f"Uma moeda antiga.", True, 'black')
dialogo_peixe11= font.render(f"Ela não valia muito…", True, 'black')
dialogo_peixe12 = font.render(f"mas era especial para mim.", True, 'black')
dialogo_peixe13 = font.render(f"Eu a encontrei antes mesmo da ilha mudar.", True, 'black')
dialogo_peixe14 = font.render(f"Costumava olhar para ela", True, 'black')
dialogo_peixe15 = font.render(f"quando me sentia sozinho.", True, 'black')
#pergunta obrigatoria: Você tem a outra chave?
pergunta3_peixe = font.render(f"  Você tem a outra chave?", True, 'white')
#
dialogo_peixe16 = font.render(f"...", True, 'black')
dialogo_peixe17 = font.render(f"Tenho.", True, 'black')
dialogo_peixe18 = font.render(f"Não gosto muito de batalhas…", True, 'black')
dialogo_peixe19 = font.render(f"Mas também não gosto de ficar sozinho o tempo todo.", True, 'black')
dialogo_peixe20 = font.render(f"Se quiser jogar um pouco comigo…", True, 'black')
dialogo_peixe21 = font.render(f"posso te entregar a chave.", True, 'black')
dialogo_peixe22 = font.render(f"talvez o lago fique menos silencioso por um tempo.", True, 'black')
dialogo_peixe23 = font.render(f"Aceita?", True, 'black')

#DIÁLOGO_CAO
font = pygame.font.Font(None, 30) 
dialogo_cao1 = font.render(f"Então… mais um visitante.", True, 'black')
dialogo_cao2 = font.render(f"Você chegou longe demais para alguém que não pertence a este lugar.", True,'black')
#pergunta obrigatoria: Estou procurando por uma estrela
pergunta1_cao = font.render(" Estou procurando por uma estrela", True, 'white')
#
dialogo_cao3 = font.render(f"...", True, 'black')
dialogo_cao4 = font.render(f"Uma estrela?", True, 'black')
dialogo_cao5 = font.render(f"Engraçado…", True, 'black')
dialogo_cao6 = font.render(f"Muitas coisas “pertencem” às pessoas até chegarem nesta ilha.", True, 'black')
dialogo_cao7 = font.render(f"Aqui, tudo passa por mim.", True, 'black')
#pergunta obrigatoria: Você pegou a estrela?
pergunta2_cao = font.render(" Você pegou a estrela?", True, 'white')
#
dialogo_cao8 = font.render(f"...", True, 'black')
dialogo_cao9 = font.render(f"Eu não pego, eu guardo coisas.", True, 'black')
dialogo_cao10 = font.render(f"Objetos perdidos, abandonados…", True, 'black')
dialogo_cao11 = font.render(f"ou... mal protegidos.", True, 'black')
dialogo_cao12 = font.render(f"Se algo chegou até mim, é porque não estava em boas mãos.", True, 'black')
dialogo_cao13 = font.render(f"Então eu cuido deles.", True, 'black')
dialogo_cao14 = font.render(f"Na verdade...", True, 'black')
dialogo_cao15 = font.render(f"Pensei que fosse algo importante.", True, 'black')
dialogo_cao16 = font.render(f"Brilhava. Chamava atenção.", True, 'black')
dialogo_cao17 = font.render(f"Mas é só um brinquedo velho, não é?", True, 'black')
dialogo_cao18 = font.render(f"Não me diga que você tem desde de filhotinho?", True, 'black')
#pergunta obrigatoria: O verdadeiro valor está no que ela representa
pergunta3_cao = font.render(" O verdadeiro valor está no que ela representa", True, 'white')
#
dialogo_cao19 = font.render(f"...", True, 'black')
#pergunta obrigatoria: Eu preciso dela para ir embora.
pergunta4_cao = font.render(" Eu preciso dela para ir embora.", True, 'white')
#
dialogo_cao20 = font.render(f"...", True, 'black')
dialogo_cao21 = font.render(f"Precisa?", True, 'black')
dialogo_cao22 = font.render(f"Todos precisam de alguma coisa.", True, 'black')
dialogo_cao23 = font.render(f"Mas poucos têm algo para oferecer em troca.", True, 'black')
#pergunta obrigatoria: Por que você controla a ilha?
pergunta5_cao = font.render(" Por que você controla a ilha?", True, 'white')
#
dialogo_cao24 = font.render(f"...", True, 'black')
dialogo_cao25 = font.render(f"Porque alguém precisava fazer isso.", True, 'black')
dialogo_cao26 = font.render(f"Antes de mim, esta ilha era desorganizada.", True, 'black')
dialogo_cao27 = font.render(f"Cada um fazia o que queria.", True, 'black')
dialogo_cao28 = font.render(f"Agora existe regra.", True, 'black')
dialogo_cao29 = font.render(f"Entrada. Saída. Trocas.", True, 'black')
#pergunta obrigatoria: Você tirou coisas dos outros também?
pergunta6_cao = font.render(" Você tirou coisas dos outros também?", True, 'white')
#
dialogo_cao30 = font.render(f"...", True, 'black')
dialogo_cao31 = font.render(f"Eu recolhi o que estava espalhado.", True, 'black')
dialogo_cao32 = font.render(f"Se eles sentem falta, talvez não soubessem cuidar direito.", True, 'black')
dialogo_cao33 = font.render(f"Valor exige responsabilidade.", True, 'black')
#pergunta obrigatoria: Eu vim até aqui, isso não mostra que sou responsavel?
pergunta7_cao = font.render(" Eu vim aqui, isso não mostra que sou responsável?", True, 'white')
#
dialogo_cao34 = font.render(f"...", True, 'black')
dialogo_cao35 = font.render(f"...", True, 'black')
dialogo_cao36 = font.render(f"Se você quer mesmo essa estrela…", True, 'black')
dialogo_cao37 = font.render(f"Vai ter que provar que merece levá-la.", True, 'black')
dialogo_cao38 = font.render(f"Você pode tentar tomá-la à força, mas duvido que consiga.", True, 'black')
dialogo_cao39 = font.render(f"Ou pode aceitar minhas regras.", True, 'black')
dialogo_cao40 = font.render(f"Uma batalha.", True, 'black')
dialogo_cao41 = font.render(f"Se vencer, a estrela é sua.", True, 'black')
dialogo_cao42 = font.render(f'E vou devolver tudo que "peguei"', True, 'black')
dialogo_cao43 = font.render(f'Mas se perder…', True, 'black')
dialogo_cao44 = font.render(f'vai embora da ilha sem ela. E nada feito.', True, 'black')
dialogo_cao45 = font.render(f'Aceita?', True, 'black')

#DERROTA
font_derrota = pygame.font.Font(None, 30) 
fala_cao_derrota0 = font_derrota.render(f'Cão:', True, 'white')
fala_cao_derrota1 = font_derrota.render(f'Como eu disse.', True, 'white')
fala_cao_derrota2 = font_derrota.render(f'Nem tudo é para qualquer um.', True, 'white')

#VITORIA
font_vitoria = pygame.font.Font(None, 25) 
fala_cao_vitoria0 = font_vitoria.render(f'Cão:', True, 'white')
fala_cao_vitoria1 = font_vitoria.render(f'Regras são regras, pegue a estrela.', True, 'white')
fala_cao_vitoria2 = font_vitoria.render(f'E saia da ilha antes que eu mude de ideia.', True, 'white')

#CONTROLES (orientação)
font = pygame.font.Font(None, 25) 
#pular diálogo
pular_dialogo = font.render(f"Pular: p ", True, 'black')
#passar dialogo
passar_dialogo = font.render(f"Próximo: espaço ", True, 'black')
#voltar ao mapa
voltar_ao_mapa = font.render(f"Voltar ao mapa: a", True, 'black')
#ao conseguir a chave
texto_chaves1 = font.render("Você conseguiu a chave!", True, 'black')
texto_chaves2 = font.render("Voltar ao mapa: a", True, 'black')
#tela de pontuação
font_p = pygame.font.Font(None, 35) 
texto_pontuaçao = font_p.render("Sair: enter", True, 'white')
#menu de batalha (tutorial de jogo)
font_p = pygame.font.Font(None, 35) 
texto_tutorial = font_p.render("Clique nos quadrados verdes, mas cuidado com os vermelhos", True, 'black')
#preços na loja
font_preco = pygame.font.Font(None, 35) 
preco_peixe = font_preco.render("R$150", True, 'yellow')
preco_sardinha = font_preco.render("R$150", True, 'yellow')
preco_leite = font_preco.render("R$300", True, 'yellow')

#QUADRADOS DAS CASAS
quadrado = pygame.Surface([30, 30]) # cria quadrado com 30 pixels de lado
quadrado_0= pygame.Rect(141, 283, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_1 = pygame.Rect(105, 20, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_2 =pygame.Rect(850, 456, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_3 = pygame.Rect(603,120, 30, 30)#cria um 'restangulo' com as cordenadas de onde ele deve ficar, a altua e a largura(x,y,A.L)
quadrado_4 = pygame.Rect(512,350, 30, 30) # cria quadrado com 30 pixels de lado

#RETANGULOS DE DETECÇÃO DOS CLIQUES NOS ITENS
#leite
retangulo_leite = pygame.Surface([108,111.5]) #tamanho do retangulo
retangulo_leite_0 = pygame.Rect(500, 290, 108,111.5)#cordenadas, altura e largura(x,y,A.L)
#biscoito de peixe
retangulo_biscoito_peixe = pygame.Surface([130, 90.5]) #tamanho do retangulo
retangulo_biscoito_peixe_0 = pygame.Rect(100, 290, 130, 90.5)#cordenadas, altura e largura(x,y,A.L)
#sardinha
retangulo_sardinha = pygame.Surface([130, 117.5]) #tamanho do retangulo
retangulo_sardinha_0 = pygame.Rect(300, 290, 130, 117.5)#cordenadas, altura e largura(x,y,A.L)

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
#quadrado branco para mostrar a quantidade de itens na loja
quadrado_itens = pygame.Surface([220, 150])
quadrado_itens.fill((225, 225, 225))
#quadrado de perguntas obrigatorias
quadrado_pergunta = pygame.Surface([560, 40])
quadrado_pergunta.fill((0, 0, 0))
#quadrado de fala cão derrota
quadrado_derrota = pygame.Surface([405, 95])
quadrado_derrota.fill((0, 0, 0))
#quadrado de fala cão vitoria
quadrado_vitoria = pygame.Surface([400, 100])
quadrado_vitoria.fill((0, 0, 0))

#FUNÇÕES:
#função para o reset do mapa e das telas
def reset_telas():
    global tela_dificuldade, tela_sena_inicial, tela_mapa, tela_dialogo, tela_loja
    global abrir_tela_de_chaves, abrir_tela_de_derrota, abrir_tela_de_vitoria
    global abrir_tela_game_over, abrir_tela_pontuacao
    global tela_dialogo_passaro, tela_dialogo_peixe, tela_dialogo_cao
    global abrir_menu_passaro, abrir_menu_peixe, abrir_menu_cao, abrir_tela_creditos
    global passar, pular, sim, nao, tempo_batalha, nota
    global tempo_batalha

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

    abrir_tela_creditos = False

    passar = 0
    pular = 0
    sim = 0
    nao = 0
    tempo_batalha = 0

def reset_status():
    global chaves, vidas, dinheiro, tarefa, nota, n_biscoito_peixe, n_sardinha, n_leite, pontos_black1, pontos_black2, pontos_black3, tempo_batalha
    global chaves, vidas, dinheiro, tarefa, nota
    global n_biscoito_peixe, n_sardinha, n_leite
    global pontos_black1, pontos_black2, pontos_black3
    global tempo_batalha, passou_do_menu_dificuldade

    passou_do_menu_dificuldade = False

    chaves = 0
    vidas = 1
    dinheiro = 300
    tarefa = 2
    nota = 0
    n_biscoito_peixe = 0
    n_sardinha = 0
    n_leite = 0
    pontos_black1 = 0
    pontos_black2 = 0
    pontos_black3 = 0
    tempo_batalha = 0

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
                    reset_status()
                    reset_telas()
                    tela_sena_inicial = True

            # ENTER NA TELA DE VITÓRIA → CRÉDITOS
            if event.key == pygame.K_RETURN and abrir_tela_de_vitoria == True:
                reset_telas()
                abrir_tela_creditos = True

            #APERTAR ENTER (mudança de tela)
            #ENTER da tela de game over
            if event.key == pygame.K_RETURN and abrir_tela_game_over == True:
                reset_telas()
                if vidas <= 0:
                    abrir_tela_de_derrota = True
                else:
                    tela_mapa = True

            #ENTER para sair da tela de pontuação
            if event.key == pygame.K_RETURN and abrir_tela_pontuacao == True:
                reset_telas()  
                abrir_tela_pontuacao = False

                if chaves == 0:
                    if nota_passaro == "A":
                        abrir_tela_de_chaves = True
                        tarefa += 1
                        chaves += 1
                    else:
                        vidas -= 1
                        abrir_tela_game_over = True

                elif chaves == 1:
                    if nota_peixe == "A":
                        abrir_tela_de_chaves = True
                        tarefa += 1
                        chaves += 1
                    else:
                        vidas -= 1
                        abrir_tela_game_over = True

                elif chaves == 2:
                    if nota_cao == "A":
                        abrir_tela_de_vitoria = True
                    else:
                        vidas -= 1
                        abrir_tela_game_over = True

            #ENTER do menu de dificuldade -> cena inicia (geral)
            if event.key == pygame.K_RETURN: 
                #ENTER -> menu de dificuldade
                if passou_do_menu_dificuldade == False:
                    if tela_dificuldade == False and tela_sena_inicial == False:
                        reset_telas()
                        tela_dificuldade = True

                    #ENTER -> menu de dificuldade → sena inicial
                    elif tela_dificuldade == True:
                        reset_telas()
                        tela_sena_inicial = True

                    #ENTER → cena inicail → mapa
                    elif tela_sena_inicial == True:
                        reset_telas()
                        tela_mapa = True

            #OPÇÕES DO MENU DE DIFICULDADES
            if tela_dificuldade == True:
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
            if event.key == pygame.K_a:
                if tela_mapa == True or abrir_tela_de_chaves == True or tela_dialogo == True or tela_dialogo_passaro == True or tela_dialogo_peixe == True or tela_dialogo_cao == True or tela_loja == True: #as telas que o mapa pode abrir
                    reset_telas()
                    tela_mapa = True
                    print("Mapa aberto")

            #PASSAGEM DE DIÁLOGO
            if tela_dialogo == True or tela_dialogo_passaro == True or tela_dialogo_peixe == True or tela_dialogo_cao == True: #só detectar nos diálogos
                if event.key == pygame.K_SPACE:
                    passar += 1 #passar diálogo
                if event.key == pygame.K_p: #seta para cima
                    pular += 1 #pular diálogo

            #ACEITAR OU RECUSAR BATALHA
            if abrir_menu_passaro == True or abrir_menu_peixe == True or abrir_menu_cao == True:
                #detectar só nos menus de batalha
                if event.key == pygame.K_s:
                    sim = sim + 1
                if event.key == pygame.K_n:
                    nao = nao + 1

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
                    if tarefa >= 2:
                        reset_telas()
                        tela_loja = True

            #SENSOR DOS CLIQUES NOS ITENS DA LOJA
            elif tela_loja:

                if retangulo_biscoito_peixe_0.collidepoint(event.pos):
                    if dinheiro >= 150:
                        n_biscoito_peixe += 1
                        dinheiro -= 150
                        vidas += 1

                elif retangulo_sardinha_0.collidepoint(event.pos):
                    if dinheiro >= 150:
                        n_sardinha += 1
                        dinheiro -= 150
                        if chaves == 0: #batalha passaro
                            pontos_black1 += 20
                        elif chaves == 1: #batalha peixe
                            pontos_black2 +=  20
                        elif chaves == 2: #batalha cao
                            pontos_black3 += 20

                elif retangulo_leite_0.collidepoint(event.pos):
                    if dinheiro >= 300 and n_leite == 0:
                        dinheiro -= 300
                        bonus_tempo = 20   # bônus reservado para a próxima batalha
                        n_leite = 1        # só pode comprar uma vez

            #CONTROLE DOS CLIQUES NOS QUADRADOS DAS BATALHAS
            if event.button == 1:
                if (em_batalha_passaro or em_batalha_peixe or em_batalha_cao) and indice_ativo != -1:
                    if quadrados_mini_game[indice_ativo].collidepoint(event.pos):

                        if em_batalha_passaro:
                            if tipo_ativo == "verde":
                                pontos_black1 += 10
                            else:
                                pontos_black1 -= 10

                        elif em_batalha_peixe:
                            if tipo_ativo == "verde":
                                pontos_black2 += 10
                            else:
                                pontos_black2 -= 10

                        elif em_batalha_cao:
                            if tipo_ativo == "verde":
                                pontos_black3 += 10
                            else:
                                pontos_black3 -= 10

                        indice_ativo = -1
                        tipo_ativo = None

                

    janela.fill((255, 255, 255))

    # TELAS ESPECIAIS 
    #tela de pontuação
    if abrir_tela_pontuacao:
        janela.blit(tela_pontuacao, (0, 0))
        janela.blit(quadrado_pontuacao, (800, 630))
        janela.blit(texto_pontuaçao, (850, 640))
        #CALCULAR OS PONTOS DOS BOSS PELA DIFICULDADE
        if dificuldade == "fácil":
            pontos_passaro = 60
            pontos_peixe = 70
            pontos_cao = 80
        elif dificuldade == "médio":
            pontos_passaro = 80
            pontos_peixe = 90
            pontos_cao = 120
        elif dificuldade == "difícil":
            pontos_passaro = 130
            pontos_peixe = 140
            pontos_cao = 150

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
        if chaves == 0:
            if pontos_black1 >= pontos_passaro:
                nota_passaro = "A"
            else:
                nota_passaro = "F"
                ir_pega_chave_passaro = True

        #peixe
        if chaves == 1:
            if pontos_black2 >= pontos_peixe:
                nota_peixe = "A"
            else:
                nota_peixe = "F"
                ir_pega_chave_peixe = True

        #cao
        '''if chaves == 2:
            if pontos_black3 >= pontos_cao:
                nota_cao = "A"
                abrir_tela_de_vitoria = True
            else:
                nota_cao = "F"
                abrir_tela_game_over = True
            #'''
        if chaves == 2:
            if pontos_black3 >= pontos_cao:
                nota_cao = "A"
            else:
                nota_cao = "F"

        font_nota = pygame.font.Font(None, 100) 
        if chaves == 0: #passaro
            if nota_passaro == "A":
                informacao_nota = font_nota.render(f"{nota_passaro}", True, 'blue')
                janela.blit(informacao_nota, (720, 500))
            elif nota_passaro == "F":
                informacao_nota = font_nota.render(f"{nota_passaro}", True, 'red')
                janela.blit(informacao_nota, (720, 500))

        if chaves == 1: #peixe
            if nota_peixe == "A":
                informacao_nota = font_nota.render(f"{nota_peixe}", True, 'blue')
                janela.blit(informacao_nota, (720, 500))
            elif nota_peixe == "F":
                informacao_nota = font_nota.render(f"{nota_peixe}", True, 'red')
                janela.blit(informacao_nota, (720, 500))

        if chaves == 2: #cao
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
        if chaves == 2: #perdeu a batalha do cão
            janela.blit(quadrado_derrota, (0, 600)) #quadrado de fala cão (derrota)
            janela.blit(fala_cao_derrota0, (10, 615))
            janela.blit(fala_cao_derrota1, (10, 635))
            janela.blit(fala_cao_derrota2, (10, 655))

    #tela de vitoria
    elif abrir_tela_de_vitoria:
        janela.blit(tela_de_vitoria, (0, 0))
        janela.blit(quadrado_vitoria, (0, 600)) #quadrado de fala cão (derrota)
        janela.blit(fala_cao_vitoria0, (10, 615))
        janela.blit(fala_cao_vitoria1, (10, 635))
        janela.blit(fala_cao_vitoria2, (10, 655))

    # MENU 
    elif tela_dificuldade or not tela_sena_inicial:
        janela.blit(menu, (0, 0))

    #MENU DE DIFICULDADE
    if tela_dificuldade:
        janela.blit(menu_dificuldade, (0, 0)) #imagem de fundo
        janela.blit(quadrado_dificuldade, (0, 638))
        #dificuldade seleciona no menu de dificuldade
        dificuldade_escolhida = font.render(f"Dificuldade: {dificuldade}", True, 'red')
        janela.blit(dificuldade_escolhida, (100, 650)) 

    #CENA INICIAL
    if tela_sena_inicial:
        janela.blit(sena_inicial, (0, 0)) #imagem de fundo
        janela.blit(texto_inicial, (140, 600)) #texto
        janela.blit(texto_inicial1, (140, 620))
        janela.blit(texto_inicial2, (140, 640))
        janela.blit(texto_inicial3, (140, 660))

    #MAPA
    if tela_mapa:
        passou_do_menu_dificuldade = True
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
            primeiro_dialogo10, primeiro_dialogo11, primeiro_dialogo12, 
            primeiro_dialogo13, primeiro_dialogo14, primeiro_dialogo15,
            primeiro_dialogo16, primeiro_dialogo17, primeiro_dialogo18,
            primeiro_dialogo19, primeiro_dialogo20, primeiro_dialogo21,
            primeiro_dialogo22, primeiro_dialogo23, primeiro_dialogo24,
            primeiro_dialogo25, primeiro_dialogo26, primeiro_dialogo27,
            primeiro_dialogo28, primeiro_dialogo29, primeiro_dialogo30,
            primeiro_dialogo31, primeiro_dialogo32, primeiro_dialogo33,
            primeiro_dialogo34, primeiro_dialogo35, primeiro_dialogo36,
            primeiro_dialogo37, primeiro_dialogo38, primeiro_dialogo39,
            primeiro_dialogo40, primeiro_dialogo41, primeiro_dialogo42,
            primeiro_dialogo43, primeiro_dialogo44, primeiro_dialogo45,
            primeiro_dialogo46, primeiro_dialogo47, primeiro_dialogo48,
            primeiro_dialogo49, primeiro_dialogo50, primeiro_dialogo51,
            primeiro_dialogo52, primeiro_dialogo53, primeiro_dialogo54,
            primeiro_dialogo55, primeiro_dialogo56, primeiro_dialogo57,
            primeiro_dialogo58, primeiro_dialogo59, primeiro_dialogo60,
            primeiro_dialogo61, primeiro_dialogo62, primeiro_dialogo63,
            primeiro_dialogo64, primeiro_dialogo65, primeiro_dialogo66,
            primeiro_dialogo67, primeiro_dialogo68, primeiro_dialogo69,
            primeiro_dialogo70, primeiro_dialogo71, primeiro_dialogo72
        ]
        
        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar == 2:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta1_gato, (10, 600))
            elif passar == 4:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta2_gato, (10, 600))
            elif passar == 21:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta3_gato, (10, 600))
            elif passar == 25:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta4_gato, (10, 600))
            elif passar == 44:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta5_gato, (10, 600))
            elif passar == 52:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta6_gato, (10, 600))
            elif passar == 58:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta7_gato, (10, 600))
            elif passar == 67:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta8_gato, (10, 600))

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
            dialogo_passaro13, dialogo_passaro14, dialogo_passaro15, 
            dialogo_passaro16, dialogo_passaro17, dialogo_passaro18, 
            dialogo_passaro19, dialogo_passaro20, dialogo_passaro21,
            dialogo_passaro22, dialogo_passaro23, dialogo_passaro24,
            dialogo_passaro25, dialogo_passaro26, dialogo_passaro27,
            dialogo_passaro28, dialogo_passaro29, dialogo_passaro30,
            dialogo_passaro31, dialogo_passaro32, dialogo_passaro33,
            dialogo_passaro34, dialogo_passaro35, dialogo_passaro36
        ]

        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar == 0:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta1_passaro, (10, 600))
            elif passar == 10:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta2_passaro, (10, 600))
            elif passar == 21:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta3_passaro, (10, 600))

            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado vai direto pro menu
            abrir_menu_passaro = True
            tela_dialogo_passaro = False
        
    #BATALHA PÁSSARO
    if em_batalha_passaro:
        janela.blit(passaro_batalha, (0, 0))

        agora = pygame.time.get_ticks()
        tempo_passado = (agora - inicio_batalha) // 1000
        tempo_restante = DURACAO_BATALHA - tempo_passado

        if tempo_restante <= 0:
            bonus_tempo = 0
            tempo_restante = 0
            em_batalha_passaro = False
            abrir_tela_pontuacao = True

            # nota por tempo
            if pontos_black1 >= pontos_passaro:
                nota_passaro = "A"
            else:
                nota_passaro = "F"
                ir_pega_chave_passaro = True

        # DESENHAR TIMER
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60

        fonte_timer = pygame.font.Font(None, 50)
        texto_timer = fonte_timer.render(
            f"{minutos:02}:{segundos:02}", True, (0, 0, 0)
        )
        janela.blit(texto_timer, (470, 20))

    if abrir_menu_passaro:
        janela.blit(menu_de_batalha_passaro, (0, 0))
        janela.blit(texto_tutorial, (130, 650)) #texto de tutorial

        if sim == 1:
            abrir_menu_passaro = False
            em_batalha_passaro = True
            inicio_batalha = pygame.time.get_ticks()

            DURACAO_BATALHA = TEMPO_BASE_BATALHA + bonus_tempo

            bonus_tempo = 0   # 
            n_leite = 0       #

            sim = 0
            nao = 0

        if sim == 1:
            nota += 1
            abrir_menu_passaro = False
            em_batalha_passaro = True
            inicio_batalha = pygame.time.get_ticks()  # <<< MUITO IMPORTANTE
            sim = 0
            nao = 0

            #COMEÇAR A BATALHA PASSARO
            if batalha_ativa:
                janela.blit(passaro_batalha, (0, 0))
                agora = pygame.time.get_ticks()
                tempo_passado = (agora - inicio_batalha) // 1000
                tempo_restante = DURACAO_BATALHA - tempo_passado

                if tempo_restante <= 0: 
                    #TEMPO ACABOU
                    DURACAO_BATALHA = TEMPO_BASE_BATALHA
                    batalha_ativa = False
                    abrir_tela_pontuacao = True
                    #calcular a nota
                    if pontos_black1 >= pontos_passaro:
                        nota_passaro = "A"
                    elif chaves == 0:
                        nota_passaro = "F"
                        ir_pega_chave_passaro = True

                minutos = max(0, tempo_restante) // 60
                segundos = max(0, tempo_restante) % 60

        elif nao == 1:
            abrir_menu_passaro = False
            sim = 0
            nao = 0
            tela_mapa = True
            ir_pega_chave_passaro = True

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
            dialogo_peixe10, dialogo_peixe11, dialogo_peixe12,
            dialogo_peixe13, dialogo_peixe14, dialogo_peixe15,
            dialogo_peixe16, dialogo_peixe17, dialogo_peixe18,
            dialogo_peixe19, dialogo_peixe20, dialogo_peixe21,
            dialogo_peixe22, dialogo_peixe23
        ]

        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar == 0:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta1_peixe, (10, 600))
            elif passar == 7:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta2_peixe, (10, 600))
            elif passar == 15:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta3_peixe, (10, 600))

            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado vai direto pro menu
            abrir_menu_peixe = True
            tela_dialogo_peixe = False

    #BATALHA PEIXE
    if em_batalha_peixe:
        janela.blit(peixe_batalha, (0, 0))

        agora = pygame.time.get_ticks()
        tempo_passado = (agora - inicio_batalha) // 1000
        tempo_restante = DURACAO_BATALHA - tempo_passado

        if tempo_restante <= 0:
            bonus_tempo = 0
            tempo_restante = 0
            em_batalha_peixe = False
            abrir_tela_pontuacao = True

            # nota por tempo
            if pontos_black1 >= pontos_peixe:
                nota_peixe = "A"
            else:
                nota_peixe = "F"
                ir_pega_chave_peixe = True

        # DESENHAR TIMER
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60

        fonte_timer = pygame.font.Font(None, 50)
        texto_timer = fonte_timer.render(
            f"{minutos:02}:{segundos:02}", True, (0, 0, 0)
        )
        janela.blit(texto_timer, (470, 20))

    if abrir_menu_peixe:
        janela.blit(menu_de_batalha_peixe, (0, 0))
        janela.blit(texto_tutorial, (130, 650)) #texto de tutorial

        if sim == 1:
            abrir_menu_peixe = False
            em_batalha_peixe = True
            inicio_batalha = pygame.time.get_ticks()

            DURACAO_BATALHA = TEMPO_BASE_BATALHA + bonus_tempo

            bonus_tempo = 0   # 
            n_leite = 0       # 

            sim = 0
            nao = 0

        if sim == 1:
            nota += 1
            abrir_menu_peixe = False
            em_batalha_peixe = True
            inicio_batalha = pygame.time.get_ticks()  # <<< MUITO IMPORTANTE
            sim = 0
            nao = 0

            #COMEÇAR A BATALHA PASSARO
            if batalha_ativa:
                janela.blit(peixe_batalha, (0, 0))
                agora = pygame.time.get_ticks()
                tempo_passado = (agora - inicio_batalha) // 1000
                tempo_restante = DURACAO_BATALHA - tempo_passado

                if tempo_restante <= 0: 
                    #TEMPO ACABOU
                    DURACAO_BATALHA = TEMPO_BASE_BATALHA
                    batalha_ativa = False
                    abrir_tela_pontuacao = True
                    #calcular a nota
                    if pontos_black2 >= pontos_peixe:
                        nota_peixe = "A"
                    elif chaves == 1:
                        nota_peixe = "F"
                        ir_pega_chave_peixe = True

                minutos = max(0, tempo_restante) // 60
                segundos = max(0, tempo_restante) % 60

        elif nao == 1:
            abrir_menu_peixe = False
            sim = 0
            nao = 0
            tela_mapa = True
            ir_pega_chave_peixe = True


    #DIALOGO CAO
    if tela_dialogo_cao:
        janela.blit(cao, (0, 0))
        janela.blit(quadrado_dialogo, (0, 638)) #quadrado branco de dialogo
        janela.blit(pular_dialogo, (10, 60)) #orientação
        janela.blit(passar_dialogo, (10, 40))
        janela.blit(voltar_ao_mapa, (10, 20))

        textos = [
            dialogo_cao1, dialogo_cao2, dialogo_cao3, dialogo_cao4,
            dialogo_cao5, dialogo_cao6, dialogo_cao7, dialogo_cao8,
            dialogo_cao9, dialogo_cao10, dialogo_cao11, dialogo_cao12,
            dialogo_cao13, dialogo_cao14, dialogo_cao15, dialogo_cao16, 
            dialogo_cao17, dialogo_cao18, dialogo_cao19, dialogo_cao20,
            dialogo_cao21, dialogo_cao22, dialogo_cao23, dialogo_cao24,
            dialogo_cao25, dialogo_cao26, dialogo_cao27, dialogo_cao28,
            dialogo_cao29, dialogo_cao30, dialogo_cao31, dialogo_cao32,
            dialogo_cao33, dialogo_cao34, dialogo_cao35, dialogo_cao36,
            dialogo_cao37, dialogo_cao38, dialogo_cao39, dialogo_cao40,
            dialogo_cao41, dialogo_cao42, dialogo_cao43, dialogo_cao44,
            dialogo_cao45
        ]

        if pular == 0: #se pular não for preencionado vai imprimir os textos
            if passar == 2:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta1_cao, (10, 600))
            elif passar == 7:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta2_cao, (10, 600))
            elif passar == 18:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta3_cao, (10, 600))
            elif passar == 19:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta4_cao, (10, 600))
            elif passar == 23:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta5_cao, (10, 600))
            elif passar == 29:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta6_cao, (10, 600))
            elif passar == 33:
                janela.blit(quadrado_pergunta, (10, 590))
                janela.blit(pergunta7_cao, (10, 600))
            
            if passar < len(textos):
                janela.blit(textos[passar], (200, 650))
        if passar >= len(textos) or pular == 1: #se pular for preencionado vai direto pro menu
            abrir_menu_cao = True
            tela_dialogo_cao = False

    #BATALHA CÃO
    if em_batalha_cao:
        janela.blit(cao_batalha, (0, 0))

        agora = pygame.time.get_ticks()
        tempo_passado = (agora - inicio_batalha) // 1000
        tempo_restante = DURACAO_BATALHA - tempo_passado

        if tempo_restante <= 0:
            bonus_tempo = 0
            tempo_restante = 0
            em_batalha_cao = False
            abrir_tela_pontuacao = True

            # nota por tempo
            if pontos_black3 >= pontos_cao:
                nota_cao = "A"
            else:
                nota_cao = "F"

        # DESENHAR TIMER
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60

        fonte_timer = pygame.font.Font(None, 50)
        texto_timer = fonte_timer.render(
            f"{minutos:02}:{segundos:02}", True, (0, 0, 0)
        )
        janela.blit(texto_timer, (470, 20))

    if abrir_menu_cao:
        janela.blit(menu_de_batalha_cao, (0, 0))
        janela.blit(texto_tutorial, (130, 650)) #texto de tutorial

        if sim == 1:
            abrir_menu_cao = False
            em_batalha_cao = True
            inicio_batalha = pygame.time.get_ticks()

            DURACAO_BATALHA = TEMPO_BASE_BATALHA + bonus_tempo

            bonus_tempo = 0   
            n_leite = 0       

            sim = 0
            nao = 0

        if sim == 1:
            nota += 1
            abrir_menu_cao = False
            em_batalha_cao = True
            inicio_batalha = pygame.time.get_ticks()  # <<< MUITO IMPORTANTE
            sim = 0
            nao = 0

            #COMEÇAR A BATALHA PASSARO
            if batalha_ativa:
                janela.blit(cao_batalha, (0, 0))
                agora = pygame.time.get_ticks()
                tempo_passado = (agora - inicio_batalha) // 1000
                tempo_restante = DURACAO_BATALHA - tempo_passado

                if tempo_restante <= 0: 
                    #TEMPO ACABOU
                    DURACAO_BATALHA = TEMPO_BASE_BATALHA
                    batalha_ativa = False
                    abrir_tela_pontuacao = True
                    #calcular a nota
                    if pontos_black3 >= pontos_cao:
                        nota_passaro = "A"
                        abrir_tela_de_vitoria = True
                    elif chaves == 2:
                        nota_passaro = "F"
                        abrir_tela_de_derrota = True

                minutos = max(0, tempo_restante) // 60
                segundos = max(0, tempo_restante) % 60

        elif nao == 1:
            abrir_menu_cao = False
            sim = 0
            nao = 0
            tela_mapa = True

    #MINI GAME DAS BATALHAS
    #desenho e controle
    if em_batalha_passaro or em_batalha_peixe or em_batalha_cao:

        agora = pygame.time.get_ticks()

        if indice_ativo == -1 or agora - tempo_quadrado > TEMPO_QUADRADO:
            indice_ativo = random.randint(0, len(quadrados_mini_game) - 1)
            tempo_quadrado = agora
            tipo_ativo = "verde" if random.random() < 0.6 else "amarelo"

        for i, q in enumerate(quadrados_mini_game):
            pygame.draw.rect(janela, (255, 255, 255), q)

            if i == indice_ativo:
                if tipo_ativo == "verde":
                    pygame.draw.rect(janela, (0, 200, 0), q) #cor do quadrado: verde
                else:
                    pygame.draw.rect(janela, (200, 0, 0), q) #cor do quadrado: vermelho

            pygame.draw.rect(janela, (0, 0, 0), q, 2)

    else:
        indice_ativo = -1
        tipo_ativo = None

    #LOJA
    if tela_loja:
        janela.blit(loja, (0, 0))

        #texto
        janela.blit(quadrado_status, (0, 530)) #quadrado branco de fundo dos status
        janela.blit(quadrado_itens, (0, 80)) #quadrado branco de fundo das quantia de itens
        janela.blit(dialogo_loja1, (500, 600))
        janela.blit(dialogo_loja2, (500, 630))
        janela.blit(voltar_ao_mapa, (800, 20))

        #informações de quantidade dos itens
        font_itens = pygame.font.Font(None, 30) 
        titulo_itens = font_itens.render(f"COMPRAS:", True, 'red')
        quantidade_biscoito_peixe = font_itens.render(f"Peixe: {n_biscoito_peixe}", True, 'black')
        quantidade_sardinha = font_itens.render(f"Sardinha: {n_sardinha}", True, 'black')
        quantidade_leite = font_itens.render(f"Leite: {n_leite}", True, 'black')
        janela.blit(titulo_itens, (10, 90))
        janela.blit(quantidade_biscoito_peixe, (10, 120))
        janela.blit(quantidade_sardinha, (10, 150))
        janela.blit(quantidade_leite, (10, 180))

        #atualização dos status:
        font = pygame.font.Font(None, 30) #definir fonte
        status_dinheiro = font.render(f"Dinheiro: R${dinheiro}", True, 'red')
        font = pygame.font.Font(None, 30) #definir fonte
        status_vidas = font.render(f"Vidas restantes: {vidas}", True, 'black')
        #status
        #(10, 540)
        #(10, 560)
        #(10, 580)
        #(10, 600)
        janela.blit(status_dinheiro, (10, 540)) #-20 pixel
        janela.blit(status_chaves, (10, 560))
        janela.blit(status_vidas, (10, 580))
        janela.blit(status_dificuldade, (10, 600))

        #colocar os quadrados de detecção
        #leite
        retangulo_leite.fill((255, 0, 0)) #colocar a cor vermelha
        janela.blit(retangulo_leite, retangulo_leite_0)
        #biscoito de peixe
        retangulo_biscoito_peixe.fill((255, 0, 0)) #colocar a cor vermelha
        janela.blit(retangulo_biscoito_peixe, retangulo_biscoito_peixe_0)
        #sardinha
        retangulo_sardinha.fill((255, 0, 0)) #colocar a cor vermelha
        janela.blit(retangulo_sardinha, retangulo_sardinha_0)

        #itens
        janela.blit(biscoito_de_peixe, (100, 290))
        janela.blit(sardinha, (300, 290))
        janela.blit(leite, (500, 290))

        #colocar o texto dos preços encima dos itens
        janela.blit(preco_peixe, (100, 390))
        janela.blit(preco_sardinha, (300, 420 ))
        janela.blit(preco_leite, (500, 410))

    elif abrir_tela_creditos == True:
        janela.blit(tela_creditos, (0, 0))

    pygame.display.flip()
    clock.tick(60)