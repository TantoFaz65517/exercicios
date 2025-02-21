import pygame
from sprites import cenario_sprite
from sprites import personagem
# Inicializa o Pygame
pygame.init()

# Configurações da janela

largura_tela = 768
altura_tela = 384
janela = pygame.display.set_mode([largura_tela, altura_tela])      

pygame.display.set_caption("Fighter Project")
clock = pygame.time.Clock()

# Fundo do jogo
janela.fill("black")

# Grupo de sprites
todas_as_sprites = pygame.sprite.Group()

# Adiciona o sprite de cenário ao grupo
cenario = cenario_sprite()
todas_as_sprites.add(cenario)

#jogador 1 e 2
jogador_1 = personagem(120, 180)
jogador_2 = personagem(320, 180)

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
    
    #movimentação
    jogador_1.move(largura_tela, largura_tela, janela, jogador_2)
    #jogador_2.move()
    
    #desenha jogadores
    jogador_1.desenhar(janela)
    jogador_2.desenhar(janela)

    pygame.display.flip()  # Atualiza a tela
    clock.tick(24)  # Limita a taxa de FPS a 60

pygame.quit()
