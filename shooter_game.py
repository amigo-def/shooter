#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as tm


class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, seas_x, seas_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(seas_x, seas_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(gameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT]:
            if self.rect.x + self.speed < 600:
                self.rect.x += self.speed
        elif keys_pressed[K_LEFT]:
            if self.rect.x - self.speed > 0:
                self.rect.x -= self.speed

    def fire(self):
        bullet_obj = Bullet('bullet.png', self.rect.centerx-12, self.rect.centery, 25, 25, 5)
        bullets.add(bullet_obj)


class Bullet(gameSprite):
    def update(self):
        if self.rect.y < 0:
            self.kill()
        else:
            self.rect.y -= self.speed

class Enemy(gameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.y = 10
            self.rect.x = randint(10, 700)
            self.speed = randint(4, 5)

class Aster(gameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.y = 10
            self.rect.x = randint(10, 700)
            self.speed = randint(1, 3)





galaxy = transform.scale(image.load('galaxy.jpg'),(800,800))
#window.blit(galaxy,(0,0))

#x1 = 100
#y1 = 100

font.init()
fon1 = font.Font(None, 33)
font_ruk = font.Font(None, 25)
ruk_text = font_ruk.render('Перезарядка', True, (255, 0, 0))

window = display.set_mode((700, 700))

mixer.init()
sound = mixer.Sound("fire.ogg")
sound.play()
mixer.music.load("space.ogg")
mixer.music.play(-1)
asters = sprite.Group()
enemies = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png", randint(10, 700), 10, 90, 90, 2)
    enemies.add(enemy)
    aster = Aster("asteroid.png", randint(10, 700), 10, 95, 95, 2)
    asters.add(aster)

bullets = sprite.Group()

clock = time.Clock()
FPS = 60

player_object = player('rocket.png', 50, 600, 100, 100, 10)
round_end =False
game_is_run =True
fire_num = 0
reload_start_time = None
game = True
while game:
    window.blit(galaxy,(0,0))
    # window.blit(sprite2,(x1, y1))
    # window.blit(sprite1,(x1, y1))
    clock.tick(FPS)
    player_object.update()
    player_object.reset()
    # enemies.update()
    # enemies.draw(window)
    bullets.update()
    bullets.draw(window)
    collides = sprite.groupcollide(enemies, bullets, True, True)
    for i in range(len(collides)):
        enemy = Enemy("ufo.png", randint(10, 700), 10, 90, 90, 2)
        enemies.add(enemy)
        aster = Aster("asteroid.png", randint(10, 700), 10, 95, 95, 2)
        asters.add(aster)
    enemies.update()
    enemies.draw(window)
    asters.update()
    asters.draw(window)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if fire_num > 5:
                    time_now = tm()
                    if time_now - reload_start_time > 2:
                        fire_num = 0
                    else:
                        window.blit(ruk_text,(player_object.rect.centerx, player_object.rect.centery))
                else:
                    fire_num += 1
                    if fire_num > 5:
                        reload_start_time = tm()
                    player_object.fire()
    
    display.update()




















































































































#window = display.set_mode((700,500))
#display.set_caption('ДОГОНЯЛКИ')
#
#background = transform.scale(image.load('background.jpg'),(700,500))
#window.blit(background,(0,0))
#
#x1 = 100
#y1 = 100
#
#sprite1 = transform.scale(image.load('hero.png'),(1000,1000))
#
##mixer.init()
##sonnd = mixer.sond("")
##sonnd.play()
##mixer.music.load("")
##mixer.music.play(-1)
##   создай 2 спрайта и размести их на сценеgame
#
#
#clock = time.Clock()
#FPS = 60
#
#game = True
#while game:
#    window.blit(background,(0,0))
#    window.blit(sprite1,(x1, y1))
#    clock.tick(FPS)
#    keys_pressed = key.get_pressed()
#    if keys_pressed[K_UP]:
#        y1 -= 10
#    if keys_pressed[K_DOWN] and y1 < 395:
#        y1 += 10
#    if keys_pressed[K_LEFT]:
#        x1 -= 10
#    if keys_pressed[K_RIGHT] and x1 < 395:
#        x1 += 10
#    for e in event.get():
#        if e.type == QUIT:
#            game = False
#    
#    display.update()
#
#from pygame import *
#
#class gameSprite(sprite.Sprite):
#    def __init__(self, player_image, player_x, player_y, player_speed):
#        super().__init__()
#        self.image = transform.scale(image.load(player_image), (65,65))
#        self.speed = player_speed
#        self.rect = self.image.get_rect()
#        self.rect.x = player_x
#        self.rect.x = player_y
#    def reset(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))
#
#window = display.set_mode((700,500))
#display.set_caption('ДОГОНЯЛКИ')
#
#background = transform.scale(image.load('background.jpg'),(700,500))
#window.blit(background,(0,0))
#
#sprite1 = transform.scale(image.load('hero.png'),(100,100))
#sprite2 = transform.scale(image.load('cyborg.png'),(100,100))
#
#clock = time.Clock()
#FPS = 60
#
#
#
#mixer.init()
#sound = mixer.Sound("kick.ogg")
#sound.play()
#mixer.music.load("jungles.ogg")
#mixer.music.play(-1)
#x1 = 100
#y1 = 100
#x2 = 600
#y2 = 300
#game = True
#while game:
#    window.blit(background,(0,0))
#    clock.tick(FPS)
#    window.blit(sprite1,(x1, y1))
#    window.blit(sprite2,(x2, y2))
#    keys_pressed = key.get_pressed()
#    if keys_pressed[K_UP]:
#        y1 -= 10
#    if keys_pressed[K_DOWN] and y1 < 395:
#        y1 += 10
#    if keys_pressed[K_LEFT]:
#        x1 -= 10
#    if keys_pressed[K_RIGHT] and x1 < 595:
#        x1 += 10
#    for e in event.get():
#        if e.type == QUIT:
#            game = False
#
#
#    display.update()

















#1
#class gameSprite(sprite.Sprite):
#    def __init__(self, player_image, player_x, player_y, seas_x, seas_y, player_speed):
#        super().__init__()
#        self.image = transform.scale(image.load(player_image),(seas_x, seas_y))
#        self.speed = player_speed
#        self.rect = self.image.get_rect()
#        self.rect.x = player_x
#        self.rect.y = player_y
#    def reset(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))
#
#class player(gameSprite):
#    def update(self):
#        keys_pressed = key.get_pressed()
#        if keys_pressed[K_UP]:
#            if sprite1.rect.y - sprite1.speed > 0:
#                sprite1.rect.y -= sprite1.speed
#                #else:
#                    #sound_effect_zapret.play()
#        elif keys_pressed[K_DOWN]:
#            if sprite1.rect.y + sprite1.speed < 425:
#                sprite1.rect.y += sprite1.speed
#                #else:
#                    #sound_effect_zapret.play()
#        elif keys_pressed[K_RIGHT]:
#            if sprite1.rect.x + sprite1.speed < 600:
#                sprite1.rect.x += sprite1.speed
#                #else:
#                    #sound_effect_zapret.play()
#        elif keys_pressed[K_LEFT]:
#            if sprite1.rect.x - sprite1.speed > 0:
#                sprite1.rect.x -= sprite1.speed
#                #else:
#                    #sound_effect_zapret.play()
#
#
#class Enemy (gameSprite):            
#    def update(self):
#        if self.rect.x <= 420:
#            self.direction = "right"
#        if self.rect.x >= 700 - 85:
#            self.direction = 'left'
#
#
#        if self.direction == 'left':
#            self.rect.x -= self.speed
#        else:
#            self.rect.x += self.speed
#        
#
#class wall(sprite.Sprite):
#    def __init__(self, red, blue, green, wall_x, wall_y, wall_width, wall_height):
#        super().__init__()
#        self.red = red
#        self.blue = blue
#        self.green = green
#        self.width = wall_width
#        self.height = wall_height
#        self.image = Surface((self.width, self.height))
#        self.image.fill((red, blue, green))
#        self.rect = self.image.get_rect()
#        self.rect.x = wall_x
#        self.rect.y = wall_y
#    def draw_wall(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))
#
#
#
#win_width = 600
#window = display.set_mode((700,500))
#display.set_caption('ДОГОНЯЛКИ')
#
#background = transform.scale(image.load('background.jpg'),(700,500))
#window.blit(background,(0,0))
#
#sprite1 = player('hero.png', 100, 135, 100, 100, 10)
#sprite2 = Enemy('cyborg.png', 400, 400, 100, 100, 10)
#final = gameSprite("treasure.png", 400, 400, 100, 100, 10)
#clock = time.Clock()
#FPS = 60
#
#
#
#mixer.init()
#sound = mixer.Sound("kick.ogg")
## sound.play()
#money = mixer.Sound("money.ogg")
#mixer.music.load("jungles.ogg")
#mixer.music.play(-1)
#x1 = 100
#y1 = 100
#x2 = 600
#y2 = 300
#wall = wall(77, 61, 33, 100, 90, 10, 240)
#game = True
#finish = False
#while game:
#    #window.blit(background,(0,0))
#    wall.draw_wall()
#    final.reset()
#    clock.tick(FPS)
#    sprite1.reset()
#    sprite1.update()
#    sprite2.reset()
#    sprite2.update()
#    
#    for e in event.get():
#        if e.type == QUIT:
#            game = False
#    
#    if finish != True:
#        if sprite.collide_rect(sprite1, final):
#            finish = True
#
#            money.play()
#
#    display.update()
#












