import pygame
BLACK = (0,0,0)

class Goleiro(pygame.sprite.Sprite):
    # Essa classe representa um Goleiro. Herda da classe Sprite do pygame
    def __init__(self, color, width, heigth):  
        super(Goleiro,self).__init__()

        self.image = pygame.Surface([width, heigth])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Desenha o goleiro
        pygame.draw.rect(self.image, color, [0, 0, width, heigth])

        self.rect = self.image.get_rect()   

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect < 0:
            self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400
    

