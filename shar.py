import pygame,random


class Shar:

    def __init__(self,start_a, x, y,l_x,l_y,rect : pygame.Rect,klacc=True,marganie=True):

        self.a = start_a
        self.x = x
        self.y = y
        self.l_x=l_x
        self.l_y=l_y
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.limit=random.randint(100,180)
        self.rect=rect
        self.klass=klacc
        self.marganie=marganie
        print(84)

    def get_rect(self):
        v=pygame.Rect(self.x-self.a,self.y-self.a,self.a*2,self.a*2)
        return v

    def draw(self, screen: pygame.Surface):
        self.screen = screen
        if self.klass:
            pygame.draw.circle(screen,self.color, [self.x, self.y], self.a)

        else:
            g=pygame.draw.rect(screen,self.color,self.get_rect(),2)
            

    def go(self):
        if isinstance(self.rect,pygame.Rect):
            print('0')
            self.rect2=self.rect
        else:
            self.rect2=self.rect.get_rect()

        if self.x+self.a>=self.rect2.right and self.l_x>0:
            self.l_x=-self.l_x
        elif self.x-self.a<=self.rect2.left and self.l_x<0:
            self.l_x=-self.l_x

        if self.y+self.a>=self.rect2.bottom and self.l_y>0:
            self.l_y=-self.l_y
        elif self.y-self.a<=self.rect2.top and self.l_y<0:
            self.l_y=-self.l_y

        if self.a<self.limit and self.marganie:
            self.a+=1
        elif self.marganie:
            self.a=50

        self.x += self.l_x
        self.y += self.l_y