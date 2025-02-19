import pygame

class cenario_sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        path = "C:/Users/20231011110027/Documents/exercicios/the-figther-project/imagens/sprites_cenario"
        self.cenario = []
        self.cenario.append(pygame.image.load(path + "/frame-1.png"))
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
        self.rect.topleft == 0,0
        


            
            
