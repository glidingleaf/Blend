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
        self.SCALE = 2


 
    def render_map(self, screen, offset):

        screen.fill((99,155,255)) # needs to be changed(background color has been hardcoded to test)
        self.tile_rects.clear()
        for layer in self.map.layers:
            
            
            for x,y, gid in layer:
                
                
                if gid != 0:
                    
                    screen.blit(pygame.transform.scale( self.tile_image(gid),(self.tile_width*self.SCALE,    self.tile_height*self.SCALE ) )  , (x*self.tile_width*self.SCALE , y*self.tile_height*self.SCALE ) - offset)
                    self.tile_rects.append(pygame.Rect(x*self.tile_width*self.SCALE,y*self.tile_height*self.SCALE,self.tile_width*self.SCALE,self.tile_height*self.SCALE))
                    
                    
                    
                    
                    
    
    def tile_rects(self):
        
        return self.tile_rects

    def drawmap(self,screen,offset):
        
        self.render_map(screen,offset)

        return screen

        