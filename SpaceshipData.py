import pygame
import random
from spaceship import Spaceship
from baddie import Baddie

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width - 20
        self.spaceship_width = 20
        self.spaceship_height = 20
        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (255,240,0))
        self.spaceship_speed = 25
        self.bullets = []
        self.bullet_width = 12
        self.bullet_height = 12
        self.bullet_color = (255,255,255)
        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (0,201,87)
        self.kill = 0
        self.score_color = (255, 255, 255)
        self.score_x = 20
        self.score_y = 30
        self.R = 1 or 2 or 3 or 4
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_a in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
            
        if pygame.K_d in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
            
        if pygame.K_w in keys:
            self.spaceship.moveUp(self.spaceship_speed)
            
        if pygame.K_s in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)

        if pygame.K_RIGHT in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
            
            
        if pygame.K_LEFT in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
            
        if pygame.K_UP in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))   
        
        if pygame.K_DOWN in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))   
             
        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)     

        if random.randint(1, self.frame_rate/2) == 1:
            self.addBaddie()
        elif random.randint(1, self.frame_rate) == 1:
            self.addStrongBaddie()
        elif random.randint(1, self.frame_rate/3) ==1:
            self.addStrongerBaddie()



        for baddie in self.baddies:
            baddie.tick(0,0,self.height, self.spaceship.x, self.spaceship.y)

        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                bullet.checkHitBaddie(x,y,w,h)
                if bullet.getHit():
                    bullet.setAlive(False)
                    baddie.decreasehitpoints(1)
                    self.kill += 1
                    bullet.hit = False


        live_bullets = []
        live_baddies = []
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)

        self.bullets = live_bullets
        self.baddies = live_baddies

        return

    def addBaddie(self):
        #random 1-4

        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width, self.baddie_height, 0, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width, self.baddie_height, random.randint(0,(self.width-self.baddie_width)), 0, self.baddie_color )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width, self.baddie_height, random.randint(0,(self.width-self.baddie_width)), self.height, self.baddie_color )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        return
    def addStrongBaddie(self):
        new_baddie = Baddie( self.baddie_width + 5, self.baddie_height + 5, self.width, random.randint(0,(self.height-self.baddie_height)), (255,255,0) )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width + 5, self.baddie_height + 5, 0, random.randint(0,(self.height-self.baddie_height)), (255,255,0) )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width + 5, self.baddie_height + 5, random.randint(0,(self.width-self.baddie_width)), 0, (255,255,0) ) 
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width + 5, self.baddie_height + 5, random.randint(0,(self.width-self.baddie_width)), self.height, (255,255,0))
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
    def addStrongerBaddie(self):
        new_baddie = Baddie( self.baddie_width + 10, self.baddie_height + 10, self.width, random.randint(0,(self.height-self.baddie_height)), (220,20,60) )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width + 10, self.baddie_height + 10, 0, random.randint(0,(self.height-self.baddie_height)), (220,20,60) )
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width + 10, self.baddie_height + 10, random.randint(0,(self.width-self.baddie_width)), 0, (220,20,60) ) 
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )
        new_baddie = Baddie( self.baddie_width + 10, self.baddie_height + 10, random.randint(0,(self.width-self.baddie_width)), self.height, (220,20,60))
        new_baddie.getAlive()
        new_baddie.setHitPoints(1)
        self.baddies.append( new_baddie )

    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        score_str = "Score: " + str(self.kill)
        self.drawTextLeft(surface, score_str, self.score_color, self.score_x, self.score_y, self.font2)

        self.spaceship.draw(surface)

        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
        return


    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return
