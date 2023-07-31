import pygame

l_x=1
class Shar:

    def __init__(self, start_a, x, y):
        self.a = start_a
        self.x = x
        self.y = y
        print(84)

    def plus5(self):
        self.a += 5

    def plus(self, y):
        self.a += y

    def draw(self, screen: pygame.Surface):
        self.screen = screen
        pygame.draw.circle(screen, [255, 255, 255], [self.x, self.y], self.a, 3)

    def go(self):
        global l_x
        if self.x<self.screen.get_width() and l_x>0:
            self.x+=1
        elif self.x==self.screen.get_width() and l_x>0:
            l_x=-1
            self.x-=1
        elif  self.x>0 and l_x<0:
            self.x-=1
        elif self.x==0 and l_x<0:
            l_x=1
            self.x+=1
