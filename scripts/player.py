import pygame
from .map import Map
from .animator import Animator
import math
import shared
import time


GRAVITY = 0.3


class Player(pygame.sprite.Sprite):

    def __init__(self, player_image_dir):

        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(100, 300)
        self.velocity = pygame.math.Vector2(0, 0)
        self.player_anim = Animator(player_image_dir)
        self.scale = shared.SCALE
        self.flipped = False
        

        # self.player_image = pygame.image.load(player_image).convert()
        # self.player_image.set_colorkey((0, 0, 0))
        # self.player_image = pygame.transform.scale(self.player_image,(self.player_image.get_width(), self.player_image.get_height()))

        # self.rect = pygame.Rect(self.pos.x, self.pos.y, self.player_image.get_width(), self.player_image.get_height())

        self.rect = pygame.Rect(self.pos.x, self.pos.y, 16*self.scale, 16*self.scale)
        self.centerpos = self.rect.center

        self.tiles = []

        self.JUMPSPEED = -5
        self.H_SPEED_LOW = 0.5
        self.H_SPEED_HIGH = 0.9
        self.FRICTION = 0.8
        self.MAXSPEED_LOW = 2.5
        self.MAXSPEED_HIGH = 3
        self.H_SPEED  = self.H_SPEED_LOW
        self.MAXSPEED  = self.MAXSPEED_LOW

        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.SHIFT_KEY = False

        self.KEYPRESSED = False
        self.JUMPED_STATE = False

        self.prev_time = time.time()
        self.cur_time = 0
        self.dt = 0
        self.LOCKED_FPS = 60
        self.eff_dt = 0

        self.dropanim_trigger = False


    def timedamper(self):

        self.cur_time = time.time()
        self.dt = self.cur_time - self.prev_time
        self.prev_time = self.cur_time

        self.eff_dt = self.dt * self.LOCKED_FPS


    def load_colliders(self, tiles):

        self.tiles = tiles

    def collision_check(self):

        collide_rects = []

        for tile in self.tiles:

            if self.rect.colliderect(tile):

                collide_rects.append(tile)

        return collide_rects


    def move(self, axis):

        

        collision_dir = {"top": False, "bottom": False,"left": False, "right": False}

        if axis == "horizontal":

            collide_rects = self.collision_check()  # checking for horizontal collision

            for tile in collide_rects:

                if self.velocity.x > 0:

                    self.rect.right = tile.left
                    collision_dir["right"] = True

                elif self.velocity.x < 0:

                    self.rect.left = tile.right
                    collision_dir["left"] = True

            if collision_dir["right"]:

                self.rect.right = tile.left
                self.velocity.x = 0

            if collision_dir["left"]:

                self.rect.left = tile.right
                self.velocity.x = 0

        else:

            collide_rects = self.collision_check()  # checking for vertical collision

            for tile in collide_rects:

                if self.velocity.y > 0:

                    self.rect.bottom = tile.top
                    collision_dir["bottom"] = True

                elif self.velocity.y < 0:

                    self.rect.top = tile.bottom
                    collision_dir["top"] = True

            if collision_dir["bottom"]:
                
                if self.dropanim_trigger:

                    self.player_anim.changeState("drop")
                    self.dropanim_trigger = False
                    

                self.velocity.y = 0
                self.JUMPED_STATE = False

            if collision_dir["top"]:

                self.velocity.y = 0

        self.pos = pygame.Vector2(self.rect.x, self.rect.y)


    def check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    self.START_KEY = True

                if event.key == pygame.K_SPACE:
                    self.UP_KEY = True

                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

                if event.key == pygame.K_d:
                    self.RIGHT_KEY = True

                if event.key == pygame.K_a:
                    self.LEFT_KEY = True

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

                if event.key == pygame.K_LSHIFT:
                    self.SHIFT_KEY = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                    self.RIGHT_KEY = False

                if event.key == pygame.K_a:
                    self.LEFT_KEY = False

                if event.key == pygame.K_SPACE:
                    self.UP_KEY = False
            
                if event.key == pygame.K_LSHIFT:
                    self.SHIFT_KEY = False
            
            


    def reset_keys(self):

        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.SHIFT_KEY = False
        self.KEYPRESSED = False

    def set_position(self, x, y):

        self.pos.x = x
        self.pos.y = y


    def event_response(self):

        self.KEYPRESSED = self.LEFT_KEY or self.RIGHT_KEY

        self.player_anim.changeState("idle")

        if self.UP_KEY == True and self.JUMPED_STATE == False:

            self.velocity.y = self.JUMPSPEED
            self.UP_KEY = False
            self.JUMPED_STATE = True

        if self.KEYPRESSED:

            if self.SHIFT_KEY:
                
                self.player_anim.changeState("run")
                self.H_SPEED = self.H_SPEED_HIGH
                self.MAXSPEED = self.MAXSPEED_HIGH
            else:

                self.player_anim.changeState("walk")
                self.H_SPEED = self.H_SPEED_LOW
                self.MAXSPEED = self.MAXSPEED_LOW
                

            if self.RIGHT_KEY == True:

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
        
        if self.velocity.y < 0 and self.JUMPED_STATE:

            self.player_anim.changeState("jump")
        
        elif self.velocity.y > 0 and self.JUMPED_STATE:

            self.player_anim.changeState("fall")

        if self.velocity.y > 1:

            self.dropanim_trigger = True
        



    def update(self, tile_rects):

        self.timedamper()

        self.check_events()

        self.load_colliders(tile_rects)
        self.event_response()

        self.rect.y += round(self.velocity.y * self.eff_dt)
        self.velocity.y += GRAVITY

        self.move("vertical")

        self.rect.x += round(self.velocity.x * self.eff_dt) 

        self.move("horizontal")

        # print(self.velocity.x * self.eff_dt)

        self.centerpos = self.rect.center

        

        

        


    def render(self, surface, offset):

        if self.velocity.x > 0:
            self.flipped = False
        elif self.velocity.x < 0:
            self.flipped = True

        # if self.velocity.y > 0 and self.JUMPED_STATE:
        #     self.player_anim.changeState("jump_up")
        # elif self.velocity.y < 0 and self.JUMPED_STATE:
        #     self.player_anim.changeState("jump_down")

        if self.flipped == True:
            
            player_image = pygame.transform.flip(self.player_anim.frameRender(),True,False)

        else:

            player_image = pygame.transform.flip(self.player_anim.frameRender(),False,False)

        surface.blit(player_image, self.pos - offset)
        

        return surface


    
