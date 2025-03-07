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
        self.tique = 1
    def update(self):
        print("update 1")
        if self.tique == 3:
            print("update 2")
        #if True:
            # Atualiza a animação do fundo
            self.tique = 0
            self.atual += 1
            if self.atual >= len(self.cenario):
                self.atual = 0  # Reinicia a animação
            self.image = self.cenario[self.atual]
        self.tique += 1

class personagem():
    def __init__(self, x, y, data, lista_sprites, animacao):
        self.tamanho = data[0]
        self.virar = False
        self.lista_animacao = self.personagem_sprite(lista_sprites, animacao)
        self.acao = 0 # 1:parado 2:corre 3: pulo 4: ataque1 4: ataque2 5:acerto 6: morte
        self.frame_index = 0
       
        self.image = self.lista_animacao[self.acao][self.frame_index]
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.pulo = False
        self.atacando = False
        self.ataque = 0
        self.tempo_ultimo_ataque = 0
        self.vida = 100
        
    def personagem_sprite(self,lista_sprites,animacao):
        #tirar sprites da lista
        lista_animacao = []
        for y, q in enumerate(animacao):
            temp_list_img = []
            for x in range(q):
                temp_img = lista_sprites.subsurface(x * self.tamanho, y * self.tamanho, self.tamanho, self.tamanho)
                temp_list_img.append(temp_img)
            lista_animacao.append(temp_list_img)
        print(lista_animacao)
        return lista_animacao
    
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

        # virar jogadores
        if alvo.rect.centerx > self.rect.centerx:
            self.virar = False
        else:
            self.virar = True
        #atualização de posição
        self.rect.x += pos_x_Player
        self.rect.y += pos_y_Player
        
    def ataq(self, surface, alvo):
        self.atacando = True
        atacando_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.virar), self.rect.y, 2 * self.rect.width, self.rect.height)
        if atacando_rect.colliderect(alvo.rect):
            alvo.vida -= 10
            print("acerto")
        pygame.draw.rect(surface, (0, 255, 0), atacando_rect)
    
    def desenhar(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, (self.rect.x, self.rect_y))