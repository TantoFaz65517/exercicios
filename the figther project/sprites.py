import pygame

class cenario_sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.cenario = []
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-1.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-2.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-3.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-4.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-5.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-6.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-7.png"))
        self.cenario.append(pygame.image.load("imagens/sprites_cenario/frame-8.png"))
        self.atual = 0
        self.img = self.cenario[self.atual]
        
        
        self.rect = self.img.get_rect()
        self.rect.topleft == 0,0
        
        

            
            
