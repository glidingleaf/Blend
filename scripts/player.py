import pygame
from .map import Map
import math


GRAVITY = 0.3

class Player():

    def __init__(self,player_image):
        
        self.pos = pygame.math.Vector2(50,50)
        self.velocity = pygame.math.Vector2(0,0)
        
        self.player_image = pygame.image.load(player_image).convert()
        self.player_image.set_colorkey((0, 0, 0))
        self.player_image = pygame.transform.scale(self.player_image,(self.player_image.get_width(), self.player_image.get_height()))
        self.player_rect = pygame.Rect(self.pos.x, self.pos.y, self.player_image.get_width(), self.player_image.get_height())
        self.tiles = []


        self.JUMPSPEED = -5
        self.H_SPEED = 0.3
        self.FRICTION = 0.8
        self.MAXSPEED = 2.0

        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        self.KEYPRESSED = False
        self.JUMPED_STATE =  False
        



    def load_colliders(self,tiles):

        self.tiles = tiles


        
    def collision_check(self):

        collide_rects = []
        
        for tile in self.tiles:
            
            
            if self.player_rect.colliderect(tile):

                collide_rects.append(tile)
            
        return collide_rects



        
    def move(self,axis):
        
        collision_dir = { "top" : False, "bottom" : False, "left" : False, "right" : False }



        if axis == "horizontal":

            collide_rects = self.collision_check() # checking for horizontal collision

            for tile in collide_rects:

                if self.velocity.x > 0:
                    
                    self.player_rect.right = tile.left
                    collision_dir["right"] = True


                elif self.velocity.x < 0:
                    
                    self.player_rect.left = tile.right
                    collision_dir["left"] = True

            if collision_dir["right"]:

                self.player_rect.right = tile.left
                self.velocity.x = 0

            if collision_dir["left"]:

                self.player_rect.left = tile.right
                self.velocity.x = 0

        else:

            collide_rects = self.collision_check()  # checking for vertical collision

            for tile in collide_rects:

    
                if self.velocity.y > 0:
                    
                    self.player_rect.bottom = tile.top
                    collision_dir["bottom"] = True
                
                elif self.velocity.y < 0:

                    self.player_rect.top = tile.bottom
                    collision_dir["top"] = True
            


            if collision_dir["bottom"]:

                self.velocity.y = 0
                self.JUMPED_STATE = False

            if collision_dir["top"]:
                
                self.velocity.y = 0


        self.pos = pygame.Vector2(self.player_rect.x, self.player_rect.y)
                              

  




    def check_events(self):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                self.START_KEY = True

            if event.key == pygame.K_UP:
                self.UP_KEY = True

            if event.key == pygame.K_DOWN:
                self.DOWN_KEY = True

            if event.key == pygame.K_RIGHT:
                self.RIGHT_KEY = True

            if event.key == pygame.K_LEFT:
                self.LEFT_KEY = True

            if event.key == pygame.K_BACKSPACE:
                self.BACK_KEY = True



    def reset_keys(self):
    
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.KEYPRESSED = False



    def set_position(self, x, y):

        self.pos.x = x
        self.pos.y = y
        


    def event_response(self):

        self.KEYPRESSED = self.LEFT_KEY or self.RIGHT_KEY

        if self.UP_KEY == True and self.JUMPED_STATE == False:

            self.velocity.y = self.JUMPSPEED
            self.UP_KEY = False
            self.JUMPED_STATE = True

        if self.KEYPRESSED:

            if self.RIGHT_KEY:

                self.velocity.x += self.H_SPEED
               
            if self.LEFT_KEY:

                self.velocity.x -= self.H_SPEED
                        
            if self.velocity.x > self.MAXSPEED:

                self.velocity.x = self.MAXSPEED

            if self.velocity.x < -self.MAXSPEED:

                self.velocity.x = -self.MAXSPEED

        else:

            self.velocity.x = self.velocity.x * self.FRICTION
            
            if abs(self.velocity.x) < 1:

                self.velocity.x = 0


           



    def  update(self,tile_rects):

        self.load_colliders(tile_rects)
        self.event_response()

        self.player_rect.y += self.velocity.y
        self.velocity.y += GRAVITY
        
        self.move("vertical")
      

        self.player_rect.x += self.velocity.x
        
        self.move("horizontal")


        #surface = self.render(surface)
        
        
    def render(self, surface, offset):
        
        surface.blit(self.player_image,self.pos - offset)
        
        return surface
        




            

        
        







    
    
    




