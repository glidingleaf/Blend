import pygame

class Camera():

    def __init__(self,player,width,height):
        
        self.player = player
        self.offset_f = pygame.math.Vector2(0, 0)
        self.offset = pygame.math.Vector2(0, 0)

        # self.focus_offset = pygame.math.Vector2(-width/2  + self.player.pos.x/2, -height/2  + self.player.pos.y/2)
        self.focus_offset = pygame.math.Vector2(width/2 - self.player.pos.x/2, height/2 + 8)
        self.width , self.height = width , height
        self.camera_limit_X = (0,500)
        self.camera_limit_Y = (100,2000)
        self.box = pygame.Rect(self.offset.x,self.offset.y,self.width,self.height)
    
    def update(self,player):

        self.offset_f.x += (player.pos.x - self.offset_f.x - self.focus_offset.x) * 0.05
        self.offset_f.y += (player.pos.y - self.offset_f.y - self.focus_offset.y) * 0.1



        # self.offset_f.x = max(int(self.offset_f.x), self.camera_limit_X[0])
        # self.offset_f.x = min(int(self.offset_f.x), self.camera_limit_X[1])

        # self.offset_f.y = max(int(self.offset_f.y), self.camera_limit_Y[0])
        # self.offset_f.y = min(int(self.offset_f.y), self.camera_limit_Y[1])
        
        self.offset.x, self.offset.y = int(self.offset_f.x), int(self.offset_f.y)

        self.box.topleft = (self.offset.x, self.offset.y)

    
