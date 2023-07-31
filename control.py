import pygame,model

def event():
    e=pygame.event.get()
    for z in e:
        if z.type==pygame.QUIT:
            exit()
