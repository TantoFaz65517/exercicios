import pygame
from sprites import cenario_sprite
from sprites import personagem

# Inicializa o Pygame
pygame.init()

# Configurações da janela
janela = pygame.display.set_mode([768, 384])
pygame.display.set_caption("Fighter Project")
clock = pygame.time.Clock()

# Grupo de sprites
todas_as_sprites = pygame.sprite.Group()

# Adiciona o sprite de cenário ao grupo
cenario = cenario_sprite()
todas_as_sprites.add(cenario)

# Player 1
player_1 = personagem(250, 250)
todas_as_sprites.add(player_1)

# Loop do jogo
loop = True
while loop:
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Atualiza sprites
    todas_as_sprites.update()

    # Limpa a tela antes de redesenhar
    janela.fill((0, 0, 0))

    # Desenha todos os sprites na tela
    todas_as_sprites.draw(janela)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(24)  # Limita a taxa de FPS a 24

pygame.quit()
