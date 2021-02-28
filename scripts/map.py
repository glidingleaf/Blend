import  pytmx
import pygame
from pytmx.util_pygame import load_pygame
import pytmx
import os

class Map():

    def __init__(self,location,window_size):

        self.map = load_pygame(location)
        
        self.tile_width = self.map.tilewidth
        self.tile_height = self.map.tileheight
        self.tile_image = self.map.get_tile_image_by_gid
        self.tile_rects =[]
        self.SCALE = 2
        os.chdir("./assets/maps")
        self.tmxdata = pytmx.TiledMap('NewWorld.tmx')
        self.window_size = window_size
        self.rendering_range = pygame.math.Vector2(20,20)


 
    def render_map(self, screen, offset,player_pos):

        screen.fill((99,155,255)) # needs to be changed(background color has been hardcoded to test)
        self.tile_rects.clear()
        count =0
        for layer in self.map.layers:
            
            
            for x,y, gid in layer:
                
                if gid != 0  and self.inBounds(x,y,offset,player_pos):
                    
                    screen.blit(pygame.transform.scale( self.tile_image(gid),(self.tile_width*self.SCALE,    self.tile_height*self.SCALE ) )  , (x*self.tile_width*self.SCALE , y*self.tile_height*self.SCALE ) - offset)

                    properties = self.tmxdata.get_tile_properties_by_gid(gid)

                    if properties["collision"] == False:

                        self.tile_rects.append(pygame.Rect(
                            x*self.tile_width*self.SCALE, y*self.tile_height*self.SCALE, self.tile_width*self.SCALE, self.tile_height*self.SCALE))

                    count += 1

        print(count)



    def tile_rects(self):
        
        return self.tile_rects


    def drawmap(self,screen,offset,player_pos):
        
        self.render_map(screen,offset,player_pos)

        return screen


    def inBounds(self, x, y, offset, player_pos):
        
        # renderX_left = self.rendering_range.x * self.tile_width + (player_pos.x - offset.x) + (self.window_size[0]/32)
        # renderX_right = self.rendering_range.x * self.tile_width - (player_pos.x - offset.x) + (self.window_size[0] / 32)
        renderX_left = self.rendering_range.x * self.tile_width 
        renderX_right = self.rendering_range.x * self.tile_width

        if int(x*self.tile_width*self.SCALE) in range(int(player_pos.x - renderX_left), int(player_pos.x + renderX_right)):
            
            if int(y*self.tile_height*self.SCALE) in range(int(player_pos.y - self.rendering_range.y * self.tile_height), int(player_pos.y + self.rendering_range.y * self.tile_height)):

                return True

        else:

            return False



        


        




        
