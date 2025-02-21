import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Luta")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

# Clock para controlar FPS
clock = pygame.time.Clock()

# Classe para os jogadores
class Lutador(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(cor)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.no_chao = True
        self.vida = 100
        

    def mover(self, teclas, esquerda, direita, pulo):
        velocidade = 5
        gravidade = 2

        # Movimentação horizontal
        if teclas[esquerda]:
            self.rect.x -= velocidade
        if teclas[direita]:
            self.rect.x += velocidade

        # Pulo
        if teclas[pulo] and self.no_chao:
            self.vel_y = -30
            self.no_chao = False

        # Aplicar gravidade
        self.vel_y += gravidade
        self.rect.y += self.vel_y

        # Limitar o chão
        if self.rect.y >= ALTURA - 80:
            self.rect.y = ALTURA - 80
            self.no_chao = True

    def atacar(self, outro_jogador, tecla_ataque, teclas):
        if teclas[tecla_ataque] and pygame.time.get_ticks() - self.tempo_ultimo_ataque > 500:
            ataque_rect = pygame.Rect(self.rect.x - 20, self.rect.y, self.rect.width + 40, self.rect.height)
            pygame.draw.rect(TELA, VERDE, ataque_rect, 2)  # Desenha a área de ataque
            if ataque_rect.colliderect(outro_jogador.rect):
                outro_jogador.vida -= 10

# Criando os jogadores
player1 = Lutador(150, ALTURA - 80, VERMELHO)
player2 = Lutador(600, ALTURA - 80, AZUL)

# Loop do jogo
rodando = True
while rodando:
    clock.tick(30)  # FPS do jogo

    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimentação dos jogadores
    player1.mover(teclas, pygame.K_a, pygame.K_d, pygame.K_w)
    player2.mover(teclas, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)

    # Ataque
    player1.atacar(player2, pygame.K_f, teclas)
    player2.atacar(player1, pygame.K_l, teclas)

    # Atualiza a tela
    TELA.fill(PRETO)

    # Desenha os jogadores
    TELA.blit(player1.image, player1.rect)
    TELA.blit(player2.image, player2.rect)

    # Desenha barras de vida
    pygame.draw.rect(TELA, VERMELHO, (50, 20, player1.vida * 2, 10))
    pygame.draw.rect(TELA, AZUL, (LARGURA - 250, 20, player2.vida * 2, 10))

    # Verifica se alguém venceu
    if player1.vida <= 0:
        print("Player 2 Venceu!")
        rodando = False
    if player2.vida <= 0:
        print("Player 1 Venceu!")
        rodando = False

    pygame.display.flip()

pygame.quit()
