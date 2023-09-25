import pygame,shar,random
screen=pygame.display.get_surface()
gosha=pygame.rect.Rect(0,0,screen.get_width(),screen.get_height())
sariki=[]
i=shar.Shar(150,500,500,2,3,gosha,False,False)
for l in range(10):

    с=shar.Shar(random.randint(10,15),
                random.randint(20,screen.get_width()-20),
                random.randint(20,screen.get_height()-20),
                random.randint(3,10),
                random.randint(3,10),
                i,
                marganie=False

                )
    sariki.append(с)
sariki.append(i)

def model():
    for l in sariki:
        l.go()
