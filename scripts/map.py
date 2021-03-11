import  pytmx
import pygame
from pytmx.util_pygame import load_pygame
import pytmx
import os
import particles

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
        self.rendering_range = pygame.math.Vector2(25, 12)
        self.fire = particles.Fire()

        # for i in range(100):
        #     self.fire.update(pygame.Surface((32,32)),(0,0))


 
    def render_map(self, screen, offset,player_pos):

        # screen.fill((99,155,255)) # needs to be changed(background color has been hardcoded to test)
        self.tile_rects.clear()
        count =0
        for layer in self.map.layers:
            
            if layer.properties["imagelayer"] == False:

                for x,y, gid in layer:
                    
                    if gid != 0  and self.inBounds(x,y,offset,player_pos):
                        
                        screen.blit(pygame.transform.scale( self.tile_image(gid),(self.tile_width*self.SCALE,    self.tile_height*self.SCALE ) )  , (x*self.tile_width*self.SCALE , y*self.tile_height*self.SCALE ) - offset)

                        properties = self.tmxdata.get_tile_properties_by_gid(gid)

                        if properties["collision"] == False:

                            self.tile_rects.append(pygame.Rect(
                                x*self.tile_width*self.SCALE, y*self.tile_height*self.SCALE, self.tile_width*self.SCALE, self.tile_height*self.SCALE))

                        if properties["id"] == 18:
                            
                            self.fire.update(screen, (x * self.tile_width * self.SCALE, y * self.tile_height * self.SCALE) - offset)

                                

                                
                                
                            


                        count += 1


        # print(count)

    def render_background(self, screen, offset):

        screen.fill((99, 155, 255))
        
        for layer in self.map.layers:

            if layer.properties["imagelayer"]:

                screen.blit(pygame.transform.scale(layer.image, (512*self.SCALE,
                                                                 288*self.SCALE)), (-offset.x * layer.properties["parallax_mul"],0))
                                                                 
                # screen.blit(layer.image, (0, 0))
                
        return screen


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





        


        




        
