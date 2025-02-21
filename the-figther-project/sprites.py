import pygame

class cenario_sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        path = "C:/Users/manoc/Desktop/exercicios/the-figther-project/imagens/sprites_cenario"
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

class personagem():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.pulo = False
        self.atacando = False
        self.ataque = 0
        self.tempo_ultimo_ataque = 0
        
    def move(self, largura_tela, altura_tela, surface, alvo):
        VEL = 10
        pos_x_Player = 0
        pos_y_Player = 0
        gravidade = 2
        
    #get inputs
        key = pygame.key.get_pressed()
        
        #só acontece se não estiver atacando, sendo atacado ou defendendo
        if self.atacando == False:
            #movimentação
            if key[pygame.K_a]:
                pos_x_Player = -VEL
            if key[pygame.K_d]:
                pos_x_Player = VEL
                
            #pulo
            if key[pygame.K_w] and self.pulo == False:
                self.vel_y = -30
                self.pulo = True
                
            #ataques
            if key[pygame.K_h] or key[pygame.K_j] or key[pygame.K_k]:
                self.ataq(surface, alvo)
                #qual tipo de ataque
                if key[pygame.K_h]:
                    self.ataque = 1
                if key[pygame.K_j]:
                    self.ataque = 2
                if key[pygame.K_k]:
                    self.ataque = 3
        
        #gravidade
        self.vel_y += gravidade    
        pos_y_Player += self.vel_y
            
        
            #limite de tela
        if self.rect.left + pos_x_Player < 0:
            pos_x_Player = -self.rect.left
        if self.rect.right +pos_x_Player > largura_tela:
            pos_x_Player = largura_tela - self.rect.right
            #limite do pulo
        if self.rect.bottom + pos_y_Player  > altura_tela - 408:
            self.vel_y = 0
            self.pulo = False
            pos_y_Player = altura_tela - 408 - self.rect.bottom
        #atualização de posição
        self.rect.x += pos_x_Player
        self.rect.y += pos_y_Player
        
    def ataq(self, surface, alvo):
        self.atacando == True
        atacando_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if atacando_rect.colliderect(alvo.rect):
            print("acerto")
        pygame.draw.rect(surface, (0, 255, 0), atacando_rect)
    
    def desenhar(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)