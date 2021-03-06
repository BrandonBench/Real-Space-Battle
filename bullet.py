#import game_mouse
import pygame
from random import randint
class Bullet():

    def __init__(self,width,height,x,y,color, direction):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 20
        self.nspeed = -20
        self.color  = (125,125,125)
        self.alive  = True
        self.hit    = False
        self.direction = direction
#        self.mousePoint = game_mouse.mouse_position
        return

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return

    def moveBullet(self):
    	if self.direction == 'up':
    	    self.y += self.speed
    	if self.direction == 'down':
    		self.y -= self.speed
    	if self.direction == 'right':
    		self.x += self.speed
    	if self.direction == 'left':
    		self.x -= self.speed
        return
    
    
    def setAlive(self,alive):
        self.alive = alive
        return
    
    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)):
                return True
                
        	return False
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return
        
    
    
    
        
