import pygame
from bullet import Bullet


class Spaceship():

    def __init__(self,width,height,x,y,color,direction = "right"):
    	self.image = pygame.image.load("ship.png")
    	self.direction = direction
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        return

    def moveLeft(self, dx, direction):
    	self.direction = direction
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit, direction):
    	self.direction = direction
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy, direction):
    	self.direction = direction
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height, direction):
        self.y += dy
        self.direction = direction
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color,direction):
        return Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color,direction)
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        if self.direction == "right":
        	surface.blit(self.image, (self.x, self.y))
        if self.direction == "left":
        	surface.blit(self.image, (self.x, self.y))
        if self.direction == "down":
        	surface.blit(self.image, (self.x, self.y))
        if self.direction == "up":
        	surface.blit(self.image, (self.x, self.y))
        
        surface.blit(self.image, (self.x, self.y))
        
        return
        
