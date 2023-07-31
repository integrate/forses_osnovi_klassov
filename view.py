import pygame,model

screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

def coop():

    model.sharik.draw(screen)
    model.e.draw(screen)
    pygame.draw.rect(screen,[255,255,255],model.gosha)
    pygame.display.flip()
    screen.fill([0,0,0])