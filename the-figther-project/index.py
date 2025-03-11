import pygame
from pygame import mixer
from sprites import cenario_sprite
from sprites import personagem
from sprites import contagem_sprite

# Inicializa o Pygame
mixer.init()
pygame.init()

# Configurações da janela
largura_tela = 768
altura_tela = 384
janela = pygame.display.set_mode([largura_tela, altura_tela])      
pygame.display.set_caption("The Fighter's Project")
clock = pygame.time.Clock()

# Cores
vermelho = (255, 0, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

# Carregar imagens
fundo_menu = pygame.image.load("the-figther-project/imagens/telas/tela1.png").convert_alpha()  # Imagem do menu
fundo_gameover = pygame.image.load("the-figther-project/imagens/telas/tela3.png").convert_alpha()  # Imagem de Game Over
fundo_transicao = pygame.image.load("the-figther-project/imagens/telas/tela2.png").convert_alpha()  # Imagem da tela de transição
vitoria_img = pygame.image.load("the-figther-project/imagens/sprites_contagem/K.O.png").convert_alpha()
versus = pygame.image.load("the-figther-project/imagens/sprites_contagem/versus.png").convert_alpha()

# Definir variáveis do jogo
contagem = 5
contador = contagem_sprite()
last_count_updade = pygame.time.get_ticks()
score = [0, 0] # [p1, p2]
fim_de_round = False
cooldown_fim_de_round = 2000

# Variáveis do jogador
tamanho_player_1 = 201
escala_player_1 = 1
offset_player_1 = [75, 85]
player_1_data = [tamanho_player_1, escala_player_1, offset_player_1]
tamanho_player_2 = 201
escala_player_2 = 1
offset_player_2 = [80, 80]
player_2_data = [tamanho_player_2, escala_player_2, offset_player_2]

# Música e som
pygame.mixer.music.load("the-figther-project/audio/consider.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1, 0.0, 5000)
som_ataque = pygame.mixer.Sound("the-figther-project/audio/ataque.mp3")

# Fundo do jogo
janela.fill("black")

# Carregar lista de sprites
samurai_1 = pygame.image.load("the-figther-project/imagens/sprites_player/samurai-1.png").convert_alpha()
samurai_2 = pygame.image.load("the-figther-project/imagens/sprites_player/samurai-2.png").convert_alpha()

# Número de frames em cada ação
samurai_1_frames = [6, 9, 8, 9, 6, 4, 5, 4, 3, 2]
samurai_2_frames = [6, 8, 8, 12, 3, 3, 6, 4, 2, 2]

# Score
fonte = pygame.font.Font("the-figther-project/fonte/FIGHTT3_.ttf", 30)

def texto(text, font, text_col, x, y):
    imge = font.render(text, True, text_col)
    janela.blit(imge, (x, y))

# Função para o menu
def menu():
    rodando = True
    while rodando:
        janela.fill((0, 0, 0))  # Limpa a tela (com fundo preto)
        
        # Desenhar a imagem de fundo do menu
        janela.blit(fundo_menu, (0, 0))  # Posições X e Y

        pygame.display.flip()  # Atualiza a tela

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER para iniciar o jogo
                    return  # Sai do loop do menu e inicia o jogo

# Função para a tela de transição
def transicao():
    rodando = True
    while rodando:
        janela.fill((0, 0, 0))  # Limpa a tela (com fundo preto)
        
        # Desenhar a imagem de fundo da tela de transição
        janela.blit(fundo_transicao, (0, 0))  # Posições X e Y

        pygame.display.flip()  # Atualiza a tela

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.time.wait(2000)  # Espera 2 segundos antes de continuar para o jogo
        return  # Sai do loop de transição e vai para o jogo

# Função para a tela de Game Over

# Sprites do cenário
todas_as_sprites = pygame.sprite.Group()

# Adiciona o sprite de cenário ao grupo
cenario = cenario_sprite()
todas_as_sprites.add(cenario)

# Função para desenhar a barra de vida
def draw_barra_vida(vida, x, y, inverter=True):
    ratio = vida / 100
    largura_max = 300
    pygame.draw.rect(janela, amarelo, (x - 2, y - 2, 304, 34))
    pygame.draw.rect(janela, azul, (x, y, 300, 30))
    if inverter:
        # Move a barra para a direita quando a vida diminui
        x = x + (largura_max - (largura_max * ratio))
    pygame.draw.rect(janela, vermelho, (x, y ,300 * ratio, 30))

# Jogadores
jogador_1 = personagem(1, 170, 235, False, player_1_data, samurai_1, samurai_1_frames, som_ataque)
jogador_2 = personagem(2, 550, 235, True, player_2_data, samurai_2, samurai_2_frames, som_ataque)

# Loop do jogo
estado_do_jogo = "menu"
while True:
    if estado_do_jogo == "menu":
        menu()
        estado_do_jogo = "transicao"

    elif estado_do_jogo == "transicao":
        transicao()
        estado_do_jogo = "jogando"

    elif estado_do_jogo == "jogando":
        # Atualiza a tela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Atualiza o fundo e os sprites
        janela.fill((0, 0, 0))  # Limpa a tela
        todas_as_sprites.update()  # Atualiza todos os sprites
        todas_as_sprites.draw(janela)  # Desenha os sprites

        if contagem <= 0:
            # Movimentação dos jogadores
            jogador_1.move(largura_tela, largura_tela, jogador_2, fim_de_round)
            jogador_2.move(largura_tela, largura_tela, jogador_1, fim_de_round)
        else:
            if (pygame.time.get_ticks() - last_count_updade) >= 1000:
                contagem -= 1
                last_count_updade = pygame.time.get_ticks()

            img = contador.get_image(contagem)
            if img:
                img_rect = img.get_rect(center=(largura_tela // 2, altura_tela // 2))
                janela.blit(img, img_rect)

        # Atualiza animação dos jogadores
        jogador_1.update()
        jogador_2.update()

        # Desenha os jogadores
        jogador_1.desenhar(janela)
        jogador_2.desenhar(janela)

        # Desenha as barras de vida
        draw_barra_vida(jogador_1.vida, 20, 20, inverter=True)
        draw_barra_vida(jogador_2.vida, 450, 20, inverter=False)
        texto("P1: " + str(score[0]), fonte, amarelo, 265, 60)
        texto("P2: " + str(score[1]), fonte, amarelo, 450, 60)

        janela.blit(versus, (320, 0))  # Exibe "Versus" na tela

        # Verifica se alguém morreu e atualiza o score
        if fim_de_round == False:
            if jogador_2.vivo == False:
                score[0] += 1
                fim_de_round = True
                fim_de_round_tempo = pygame.time.get_ticks()
        if fim_de_round == False:
            if jogador_1.vivo == False:
                score[1] += 1
                fim_de_round = True
                fim_de_round_tempo = pygame.time.get_ticks()

        if fim_de_round == True:
            janela.blit(vitoria_img, (290, 120))  # Exibe o "K.O" na tela
            if pygame.time.get_ticks() - fim_de_round_tempo > cooldown_fim_de_round:
                contagem = 5
                jogador_1 = personagem(1, 170, 235, False, player_1_data, samurai_1, samurai_1_frames, som_ataque)
                jogador_2 = personagem(2, 550, 235, True, player_2_data, samurai_2, samurai_2_frames, som_ataque)
                fim_de_round = False

        pygame.display.flip()  # Atualiza a tela
        clock.tick(24)  # Limita a taxa de FPS a 60
