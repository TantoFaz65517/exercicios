import pygame

class cenario_sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        path = "C:/Users/20231011110027/Documents/exercicios/the-figther-project/imagens/sprites_cenario"
        self.cenario = []
        self.cenario.append(pygame.image.load(path + "/frame-1.png"))
        self.cenario.append(pygame.image.load(path + "/frame-2.png"))
        self.cenario.append(pygame.image.load(path + "/frame-3.png"))
        self.cenario.append(pygame.image.load(path + "/frame-4.png"))
        self.cenario.append(pygame.image.load(path + "/frame-5.png"))
        self.cenario.append(pygame.image.load(path + "/frame-6.png"))
        self.cenario.append(pygame.image.load(path + "/frame-7.png"))
        self.cenario.append(pygame.image.load(path + "/frame-8.png"))
        self.atual = 0
        self.image = self.cenario[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)  # Corrigido para atribuição correta

    def update(self):
        # Atualiza a animação do fundo
        self.atual += 1
        if self.atual >= len(self.cenario):
            self.atual = 0  # Reinicia a animação
        self.image = self.cenario[self.atual]

# Inicializa o Pygame
pygame.init()

# Configurações da janela
janela = pygame.display.set_mode([768, 384])
pygame.display.set_caption("Fighter Project")
clock = pygame.time.Clock()

# Fundo do jogo
img_fundo = pygame.image.load("C:/Users/20231011110027/Documents/exercicios/the-figther-project/imagens/cenarios_acriativos-42.gif")

# Grupo de sprites
todas_as_sprites = pygame.sprite.Group()

# Adiciona o sprite de cenário ao grupo
cenario = cenario_sprite()
todas_as_sprites.add(cenario)

# Player 1
img_player_1 = pygame.image.load("C:/Users/20231011110027/Documents/exercicios/the-figther-project/imagens/personagem2.png")
pos_y_player_1 = 95
pos_x_player_1 = 150
vel_mov = 20

# Loop do jogo
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        pos_y_player_1 -= vel_mov
    if teclas[pygame.K_DOWN]:
        pos_y_player_1 += vel_mov
    if teclas[pygame.K_RIGHT]:
        pos_x_player_1 += vel_mov
    if teclas[pygame.K_LEFT]:
        pos_x_player_1 -= vel_mov

    # Limites do cenário
    if pos_x_player_1 <= 0:
        pos_x_player_1 = 0
    elif pos_x_player_1 >= 610:
        pos_x_player_1 = 610
    if pos_y_player_1 <= 0:
        pos_y_player_1 = 0
    elif pos_y_player_1 >= 135:
        pos_y_player_1 = 135

    # Atualiza a tela
    janela.fill((0, 0, 0))  # Limpa a tela (preenchendo com a cor preta)
    janela.blit(img_fundo, (0, 0))  # Desenha o fundo
    janela.blit(img_player_1, (pos_x_player_1, pos_y_player_1))  # Desenha o jogador
    todas_as_sprites.update()  # Atualiza todos os sprites (animação do fundo)
    todas_as_sprites.draw(janela)  # Desenha os sprites na tela

    pygame.display.flip()  # Atualiza a tela
    clock.tick(20)  # Limita a taxa de FPS a 60

pygame.quit()
