import  pytmx
import pygame
from pytmx.util_pygame import load_pygame
import os

class Map():

    def __init__(self,location):

        self.map = load_pygame(location)
        
        self.tile_width = self.map.tilewidth
        self.tile_height = self.map.tileheight
        self.tile_image = self.map.get_tile_image_by_gid
        self.tile_rects =[]


 
    def render_map(self, screen):

        screen.fill((99,155,255)) # needs to be changed(background color has been hardcoded to test)
        self.tile_rects.clear()
        for layer in self.map.layers:
            
            
            for x,y, gid in layer:
                
                
                if gid != 0:
                    
                    screen.blit(self.tile_image(gid), (x*self.tile_width,y*self.tile_height))
                    self.tile_rects.append(pygame.Rect(x*self.tile_width,y*self.tile_height,self.tile_width,self.tile_height))
                    
                    
                    
                    
                    
    
    def tile_rects(self):
        
        return self.tile_rects

    def drawmap(self,screen):
        
        #surface = pygame.Surface((512, 288))
        self.render_map(screen)
        return screen

        