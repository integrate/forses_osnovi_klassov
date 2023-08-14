import pygame

screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
import model

def coop():
    for l in model.sariki:
        l.draw(screen)
    pygame.draw.rect(screen,[255,255,255],model.gosha,1)
    pygame.display.flip()
    screen.fill([0,0,0])