from pygame import * 
window = display.set_mode((700,500)) 
background = Surface((700,500)) 
background.fill((0,0,0)) 
 
class Player(sprite.Sprite): 
    def __init__(self,x,y,w,h): 
        super().__init__()
        self.w = w 
        self.h = h 
        self.xspeed = 2 
        self.yspeed = 2 
        self.rect_ = Surface((self.w,self.h)) 
        self.rect_.fill((255,0,0)) 
        self.rect = self.rect_.get_rect() 
        self.rect.x = x  
        self.rect.y = y 
 
    def Ballmove(self): 
        if self.rect.y <= 0 or self.rect.y > 500: 
            self.yspeed *= -1 
        if self.rect.x >= 700 or self.rect. x <= 0: 
            self.rect.y = 245 
            self.rect.x = 365 
        self.rect.x += self.xspeed 
        self.rect.y += self.yspeed

    def player1Move(self):
        ev = key.get_pressed()
        if ev[K_w] and self.rect.y >= 0:
            self.rect.y -= self.yspeed
        if ev[K_s] and self.rect.y <= 500-self.h:
            self.rect.y += self.yspeed

    def player2Move(self):
        ev = key.get_pressed()
        if ev[K_DOWN] and self.rect.y <= 500-self.h: 
            self.rect.y += self.yspeed
        if ev[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.yspeed
 
    def set_(self):
        window.blit(self.rect_,(self.rect.x,self.rect.y))


player1 = Player(10,190,15,80)
player2 = Player(655,190,15,80)

ball = Player(345,245,5,5)

pl_group = sprite.Group()
pl_group.add(player1)
pl_group.add(player2)

ball_group = sprite.Group()
ball_group.add(ball)

def collider():
    sprite_group = sprite.groupcollide(
        pl_group,ball_group, False, False
    )
    if len(sprite_group) != -0:
        ball.xspeed *= -1

frames = 60
clock = time.Clock()
running = True
game = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    window.blit(background,(0,0))
    if game:
        player1.set_()
        player2.set_()
        ball.set_()
        player1.player1Move()
        player2.player2Move()
        ball.Ballmove()

        collider()
    display.update()
    clock.tick(frames)