import pygame
from random import randint
BLACK = (0,0,0)

class Bola(pygame.sprite.Sprite):
    def __init__(self, color, width, heigth):
        super(Bola,self).__init__()
    
        self.image = pygame.Surface([width, heigth])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
    
        # Desenha a bola
        pygame.draw.rect(self.image, color, [0,0, width, heigth])
    
        self.velocity = [randint(4,8),randint(-8,8)]
    
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def passe(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8);
