import pygame
import random

class Baddie():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.color  = color
        self.alive  = True
        self.speed  = 1
        self.hit_points = 1
        self.lives= 10
        return
        
    def setHitPoints(self, hit_points):
        self.hit_points = hit_points

    def decreasehitpoints(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.setAlive(False)

    def tick(self,back_wall,upper_wall,lower_wall, sx, sy):
        if self.x > sx:
            self.new_x = self.x - self.speed
        else:
            self.new_x = self.x + self.speed
            
        if self.y > sy:
            self.new_y = self.y - self.speed
        else:
            self.new_y = self.y + self.speed
            
        if self.new_x < back_wall:
            self.setAlive(False)
        else:
            self.x = self.new_x
        if self.new_x < back_wall:
            self.setAlive(False)
            self.lives -= 1
            
        else:
            self.x = self.new_x
        if self.new_y < upper_wall:
            self.new_y = upper_wall
        elif self.new_y + self.height > lower_wall:
            self.new_y = lower_wall - self.height
        self.y = self.new_y
        return self.alive

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)







