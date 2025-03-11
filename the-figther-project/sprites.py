import pygame
class cenario_sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        path = "the-figther-project/imagens/sprites_cenario"
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
        if self.tique == 3:
            # Atualiza a animação do fundo
            self.tique = 0
            self.atual += 1
            if self.atual >= len(self.cenario):
                self.atual = 0  # Reinicia a animação
            self.image = self.cenario[self.atual]
        self.tique += 1

class contagem_sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        path = "the-figther-project/imagens/sprites_contagem"
        self.contagem = []
        self.contagem.append(pygame.image.load(path + "/lutar!.png"))
        self.contagem.append(pygame.image.load(path + "/lutar!.png"))
        self.contagem.append(pygame.image.load(path + "/numero-1.png"))
        self.contagem.append(pygame.image.load(path + "/numero-2.png"))
        self.contagem.append(pygame.image.load(path + "/numero-3.png"))
        
        
    
    def get_image(self, number):
        if 0 <= number < len(self.contagem):
            return self.contagem[number]
        return None


class personagem():
    def __init__(self, player, x, y, virar, data, lista_sprites, animacao, som):
        self.player = player
        self.tamanho = data[0]
        self.escala_image = data[1]
        self.offset = data[2]
        self.virar = virar
        self.lista_animacao = self.personagem_sprite(lista_sprites, animacao)
        self.acao = 0 # 0:parado 1:andar 2: correr 3: pular 4:morrer 5: ataque1 6: ataque2 7: ataque3 8: dano 9: defesa
        self.frame_index = 0
        self.image = self.lista_animacao[self.acao][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 40, 120))
        self.vel_y = 0
        self.correr = False
        self.pulo = False
        self.atacando = False
        self.ataque = 0
        self.tempo_ultimo_ataque = 0
        self.som_ataque = som
        self.acerto = False
        self.vida = 100
        self.vivo = True
        
    def personagem_sprite(self,lista_sprites,animacao):
        #tirar sprites da lista
        lista_animacao = []
        for y, q in enumerate(animacao):
            temp_list_img = []
            for x in range(q):
                temp_img = lista_sprites.subsurface(x * self.tamanho, y * self.tamanho, self.tamanho, self.tamanho)
                
                temp_list_img.append(pygame.transform.scale(temp_img, (self.tamanho * self.escala_image, self.tamanho * self.escala_image)))
            lista_animacao.append(temp_list_img)
        return lista_animacao
    
    def move(self, largura_tela, altura_tela, alvo, fim_de_round):
        VEL = 10
        pos_x_Player = 0
        pos_y_Player = 0
        gravidade = 2
        self.correr = False
        #self.ataque = 0
        
    #get inputs
        key = pygame.key.get_pressed()
        
        #só acontece se não estiver atacando, sendo atacado ou defendendo
        if self.atacando == False and self.vivo == True and fim_de_round == False:
            if self.player == 1:
                #movimentação
                if key[pygame.K_a]:
                    pos_x_Player = -VEL
                    self.correr = True
                if key[pygame.K_d]:
                    pos_x_Player = VEL
                    self.correr = True
                    
                #pulo
                if key[pygame.K_w] and self.pulo == False:
                    self.vel_y = -30
                    self.pulo = True
                    
                #ataques
                if key[pygame.K_h] or key[pygame.K_j] or key[pygame.K_k]:
                    self.ataq(alvo)
                    
                    #qual tipo de ataque
                    if key[pygame.K_h]:
                        self.ataque = 1
                    if key[pygame.K_j]:
                        self.ataque = 2
                    if key[pygame.K_k]:
                        self.ataque = 3
            #player 2
            if self.player == 2:
                #movimentação
                if key[pygame.K_LEFT]:
                    pos_x_Player = -VEL
                    self.correr = True
                if key[pygame.K_RIGHT]:
                    pos_x_Player = VEL
                    self.correr = True
                    
                #pulo
                if key[pygame.K_UP] and self.pulo == False:
                    self.vel_y = -30
                    self.pulo = True
                    
                #ataques
                if key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]:
                    self.ataq(alvo)
                    
                    #qual tipo de ataque
                    if key[pygame.K_KP1]:
                        self.ataque = 1
                    if key[pygame.K_KP2]:
                        self.ataque = 2
                    if key[pygame.K_KP3]:
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

        #cooldown ataque
        if self.tempo_ultimo_ataque > 0:
            self.tempo_ultimo_ataque -= 5
        
    def update(self):
    # Definir cooldown de animação
        if self.acao == 6:  # Se for ataque 2
            animacao_cooldown = 40  # Reduzindo o tempo (mais rápido)
        else:
            animacao_cooldown = 120  # Tempo normal

        # Checar qual animação fazer
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            self.update_acao(4) #4 morrer
        elif self.acerto == True:
            self.update_acao(8) # dano acerto
        elif self.atacando:
            if self.ataque == 1:
                self.update_acao(5)  # Ataque 1
            elif self.ataque == 2:
                self.update_acao(6)  # Ataque 2 (mais rápido agora)
            else:
                self.update_acao(7)  # Ataque 3
        elif self.pulo:
            self.update_acao(3)  # Pular
        elif self.correr:
            self.update_acao(2)  # Correr
        else:
            self.update_acao(0)  # Parado

        # Atualizar animação
        self.image = self.lista_animacao[self.acao][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animacao_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
            # Resetar loop
            if self.frame_index >= len(self.lista_animacao[self.acao]):
                #checar se o player esta morto e encerrar anima
                if self.vivo == False:
                    self.frame_index = len(self.lista_animacao[self.acao]) - 1
                else:
                    self.frame_index = 0
                    if self.acao in [5, 6, 7]:  # Se o ataque terminou
                        self.atacando = False
                        self.tempo_ultimo_ataque = 50
                    #verificar se levou dano
                    if self.acao == 8:
                        self.acerto = False
                        self.atacando = False
                        self.tempo_ultimo_ataque = 50
                    
    def ataq(self, alvo):
        if self.tempo_ultimo_ataque == 0:
            self.atacando = True
            self.som_ataque.play()
            atacando_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.virar), self.rect.y, 2 * self.rect.width, self.rect.height)
            if atacando_rect.colliderect(alvo.rect):
                alvo.vida -= 10
                alvo.acerto  = True
            
    
    def update_acao(self, nova_acao):
        #checar numero de sprites em cada animacao
        if nova_acao != self.acao:
            self.acao = nova_acao
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    def desenhar(self, surface):
        img = pygame.transform.flip(self.image, self.virar, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.escala_image), self.rect.y - (self.offset[1] * self.escala_image)))