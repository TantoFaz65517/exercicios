import pygame
from sprites import cenario_sprite
from sprites import personagem
from sprites import contagem_sprite
# Inicializa o Pygame
pygame.init()

# Configurações da janela

largura_tela = 768
altura_tela = 384
janela = pygame.display.set_mode([largura_tela, altura_tela])      

pygame.display.set_caption("The Fighter's Project")
clock = pygame.time.Clock()

#cores
vermelho = (255, 0, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

#definir variaveis do jogo
contagem = 5
contador = contagem_sprite()
last_count_updade = pygame.time.get_ticks()
#variavel player
tamanho_player_1 = 201
escala_player_1 = 1
offset_player_1 = [75, 85]
player_1_data = [tamanho_player_1, escala_player_1, offset_player_1]
tamanho_player_2 = 201
escala_player_2 = 1
offset_player_2 = [80, 80]
player_2_data = [tamanho_player_2, escala_player_2, offset_player_2]
# Fundo do jogo
janela.fill("black")

#carregar lista de sprites
samurai_1 = pygame.image.load("the-figther-project/imagens/sprites_player/samurai-1.png").convert_alpha()
samurai_2 = pygame.image.load("the-figther-project/imagens/sprites_player/samurai-2.png").convert_alpha()

#numero de frames em cada ação

samurai_1_frames = [6, 9, 8, 9, 6, 4, 5, 4, 3, 2]
samurai_2_frames = [6, 8, 8, 12, 3, 3, 6, 4, 2, 2]
# Grupo de sprites
todas_as_sprites = pygame.sprite.Group()

# Adiciona o sprite de cenário ao grupo
cenario = cenario_sprite()
todas_as_sprites.add(cenario)
#função para fazer as barras de vida
def draw_barra_vida(vida, x, y):
    ratio = vida / 100
    pygame.draw.rect(janela, amarelo, (x - 2, y - 2, 304, 34))
    pygame.draw.rect(janela, azul, (x, y, 300, 30))
    pygame.draw.rect(janela, vermelho, (x, y ,300 * ratio, 30))
    
#jogador 1 e 2
jogador_1 = personagem(1, 170, 235, False, player_1_data, samurai_1, samurai_1_frames)
jogador_2 = personagem(2, 550, 235, True, player_2_data, samurai_2, samurai_2_frames)

# Loop do jogo
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Atualiza a tela
    janela.fill((0, 0, 0))  # Limpa a tela (preenchendo com a cor preta)
    todas_as_sprites.update()  # Atualiza todos os sprites (animação do fundo)
    todas_as_sprites.draw(janela)  # Desenha os sprites na tela
   
    if contagem <= 0:
        #movimentação
        jogador_1.move(largura_tela, largura_tela, janela, jogador_2)
        jogador_2.move(largura_tela, largura_tela, janela, jogador_1)
    else:
        if (pygame.time.get_ticks() - last_count_updade) >= 1000:
            contagem -= 1
            last_count_updade = pygame.time.get_ticks()
            print(contagem)
        img = contador.get_image(contagem)
        if img:
            img_rect = img.get_rect(center=(largura_tela // 2, altura_tela // 2))
            janela.blit(img, img_rect)


    
    #atualizar animação
    jogador_1.update()
    jogador_2.update()

    #desenha jogadores
    jogador_1.desenhar(janela)
    jogador_2.desenhar(janela)

     #barras de vida
    draw_barra_vida(jogador_1.vida, 20, 20)
    draw_barra_vida(jogador_2.vida, 450, 20)

    pygame.display.flip()  # Atualiza a tela
    clock.tick(24)  # Limita a taxa de FPS a 60

pygame.quit()
