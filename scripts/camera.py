import pygame

class Camera():

    def __init__(self,player,width,height):
        
        self.player = player
        self.offset_f = pygame.math.Vector2(0, 0)
        self.offset = pygame.math.Vector2(0, 0)

        self.focus_offset = pygame.math.Vector2(-width/2  + self.player.pos.x/2, -height/2  + self.player.pos.y/2)
        self.width , self.height = width , height
        self.C = 0
    
    def update(self,player):

        self.offset_f.x += (player.pos.x - self.offset_f.x + self.focus_offset.x) /5
        self.offset_f.y += (player.pos.y - self.offset_f.y + self.focus_offset.y) /5

        self.offset.x, self.offset.y = int(self.offset_f.x), int(self.offset_f.y)

        # self.offset.x = int(self.offset_f.x)

        # self.offset.y = max( int(self.offset.y), self.C)
        