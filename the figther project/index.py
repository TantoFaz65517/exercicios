import pygame
import sprites


janela = pygame.display.set_mode([768, 384])

pygame.display.set_caption("fighter project")

clock = pygame.time.Clock()

img_fundo = pygame.image.load("C:/Users/manoc/Desktop/imagens/cenarios_acriativos-45(2).gif")

todas_as_sprites = pygame.sprite.Group()

cenario = sprites.cenario_sprite

todas_as_sprites.add(cenario)
#player 1 assets
img_player_1 = pygame.image.load("C:/Users/manoc/Desktop/imagens/personagem2.png")
pos_y_player_1 = 95
pos_x_player_1 = 150
vel_mov = 20
loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    teclas = pygame.key.get_pressed()
#movimentação do jogador 
    if teclas[pygame.K_UP]:
        pos_y_player_1 -= vel_mov
        
    if teclas[pygame.K_DOWN]:
        pos_y_player_1 += vel_mov
        
    if teclas[pygame.K_RIGHT]:
        pos_x_player_1 += vel_mov
        
    if teclas[pygame.K_LEFT]:
        pos_x_player_1 -= vel_mov
#barreira do cenário        
    if pos_x_player_1 <= 0:
        pos_x_player_1 = 0
    elif pos_x_player_1 >= 610:
        pos_x_player_1 = 610
        
    if pos_y_player_1 <= 0:
        pos_y_player_1 = 0
    elif pos_y_player_1 >= 135:
        pos_y_player_1 = 135
    print(pos_x_player_1, pos_y_player_1)
    janela.blit(img_fundo, (0,0))
    janela.blit(img_player_1, (pos_x_player_1, pos_y_player_1))
    todas_as_sprites.draw(janela)
    todas_as_sprites.update()
    pygame.display.flip()
    clock.tick(24)