import  pytmx
import pygame
from pytmx.util_pygame import load_pygame
import pytmx
import os
import particles
import shared

class Map():

    def __init__(self,location,window_size):

        self.map = load_pygame(location)
        
        self.tile_width = self.map.tilewidth
        self.tile_height = self.map.tileheight
        self.tile_image = self.map.get_tile_image_by_gid
        self.tile_rects =[]
        self.SCALE = shared.SCALE

        os.chdir("./assets/maps")
        self.tmxdata = pytmx.TiledMap('NewWorld.tmx')

        self.window_size = window_size
        self.rendering_range = pygame.math.Vector2(25, 12)
        self.fire = particles.Fire()
        
        self.width = self.map.width
        self.height = self.map.height
        self.MARGIN = self.SCALE

        # for i in range(100):
        #     self.fire.update(pygame.Surface((32,32)),(0,0))

    


    
 
    def render_map(self, screen, offset,player_pos):

        # screen.fill((99,155,255)) # needs to be changed(background color has been hardcoded to test)
        self.tile_rects.clear()
        count = 0
        

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


    def drawmap(self,screen,offset,player_pos,camera_box):
        
        # self.render_map(screen,offset,player_pos)
        self.Renderx(screen,offset,camera_box)

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

    
    def Renderx(self,screen,offset,camera_box):
        
        self.tile_rects.clear()
        count = 0
        for y in range(round(int(camera_box.top/(self.tile_height*self.SCALE))-self.MARGIN),round(int(camera_box.bottom/(self.tile_height*self.SCALE)))+self.MARGIN):

            for x in range(round(int(camera_box.left/(self.tile_width*self.SCALE)))-self.MARGIN, round(int(camera_box.right/(self.tile_width*self.SCALE)))+self.MARGIN):

                for layer in self.map.layers:

                    if layer.properties["imagelayer"] == False:
                        
                        new_y = y*self.tile_height*self.SCALE
                        new_x = x*self.tile_width*self.SCALE

                        if self.in_map(layer.data,y,x):
                            gid = layer.data[y][x]

                            # print(gid) 
                            #new_ y and new_x can go out of bounds for layer.data

                            if gid != 0:

                                
                                image = pygame.transform.scale(self.tile_image(gid), (self.tile_width*self.SCALE,self.tile_height*self.SCALE))

                                screen.blit(image, (new_x - offset.x, new_y -offset.y))

                                properties = self.tmxdata.get_tile_properties_by_gid(gid)

                                if properties["collision"] == False:

                                    self.tile_rects.append(pygame.Rect(
                                        new_x, new_y, self.tile_width*self.SCALE, self.tile_height*self.SCALE))

                                if properties["id"] == 18:

                                    self.fire.update(
                                        screen, (new_x , new_y) - offset)
                                    
                                count = count +1
        # print(count)
        # print(len(self.tile_rects))



    def in_map(self,data, y, x):

        try:
            data[int(y)][int(x)]

        except (ValueError, IndexError):
            return False
        else:
            return True














        




        







        


        




        
