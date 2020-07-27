import sys
import pygame
from goleiro import Goleiro
from bola import Bola

pygame.init()

# Cores 
BLACk = (0,0,0)
WHITE = (255,255,255)
COR = (7,50,67)
# Abre uma janela 
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

goleiroA = Goleiro(WHITE, 10, 100)
goleiroA.rect.x = 20
goleiroA.rect.y = 200

goleiroB = Goleiro(WHITE, 10, 100)
goleiroB.rect.x = 670
goleiroB.rect.y = 200

bola = Bola(COR, 10, 10)
bola.rect.x = 345
bola.rect.y = 195

sprite_list = pygame.sprite.Group()

sprite_list.add(goleiroA)
sprite_list.add(goleiroB)
sprite_list.add(bola)

carryOn = True

clock = pygame.time.Clock()

golsA = 0
golsB = 0 

clock = pygame.time.Clock()
# Loop principal
while carryOn:
    # Loop dos eventos principais
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
    # Move os goleiros quanda aperta A/S ou Setas para o outro goleiro
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        goleiroA.moveUp(5)
    if keys[pygame.K_s]:
        goleiroA.moveDown(5)
    if keys[pygame.K_UP]:
        goleiroB.moveUp(5)
    if keys[pygame.K_DOWN]:
        goleiroB.moveDown(5)

    # Logica do Game
    sprite_list.update()

    # Verifica se a bola esta batendo em alguma das 4 paredes
    if bola.rect.x >= 690:
        golsA+=1
        bola.velocity[0] = -bola.velocity[0]
    if bola.rect.x <= 0:
        golsB+=1
        bola.velocity[0] = -bola.velocity[0]
    if bola.rect.y > 490:
        bola.velocity[1] = -bola.velocity[1]
    if bola.rect.y < 0:
        bola.velocity[1] = -bola.velocity[1]

    # Detecta colisao entre os goleiros e a bola
    if pygame.sprite.collide_mask(bola, goleiroA) or pygame.sprite.collide_mask(bola, goleiroB):
      bola.passe()

    # Desenhos do jogo
    screen.fill(BLACk)
    pygame.draw.line(screen,WHITE, [349,0], [349,500], 5)
    sprite_list.draw(screen)

    #  Printa os Gols :
    font = pygame.font.Font(None, 74)
    text = font.render(str(golsA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(golsB), 1, WHITE)
    screen.blit(text, (420,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()