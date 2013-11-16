import pygame
from bullet import Bullet


class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.imager = pygame.image.load("playerShipRight.png")
        self.imagel = pygame.image.load("playerShipLeft.png")
        self.imageu = pygame.image.load("playerShipUp.png")
        self.imaged = pygame.image.load("playerShipdwn.png")
        self.direction = None
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.Living = True
        self.hit    = False
        self.alive  = True
        return
    
    def setAlive(self,alive):
        self.alive = alive
        return

    def getAlive(self):
        return self.alive


    def moveLeft(self, dx):
        self.direction = "left"
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.direction = "right"
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy):
        self.direction = "down"
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        self.direction = "up"
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color,direction):
        self.direction = direction
        return Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color,direction)
    
    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)):
                self.Living = False
                return True
            return False


    def draw(self, surface):
        if self.Living == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height)
        
            if self.direction == "right":
                surface.blit(self.imager, (self.x, self.y))
            if self.direction == "left":
                surface.blit(self.imagel, (self.x, self.y))
            if self.direction == "up":
                surface.blit(self.imaged, (self.x, self.y))
            if self.direction == "down":
                surface.blit(self.imageu, (self.x, self.y))
            return

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x,y,w,h):
            self.setAlive(False)
            self.hit = True
        
