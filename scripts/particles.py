import pygame
import random
import math
import shared



class Particles:

    def __init__(self):

        self.side = random.randint(round(shared.TILESIZE*shared.SCALE*0.1), round(shared.TILESIZE*shared.SCALE*0.2))
        # self.side = random.randint(3, 5)
        self.velocity = pygame.math.Vector2(0, 0)
        self.location = pygame.Vector2(shared.TILESIZE * shared.SCALE * 0.5,
                                       shared.TILESIZE * shared.SCALE * 1.5) - (self.side * 0.5, self.side * 0.5)

        self.velocity.x = random.randint(-10, 10)/10
        self.velocity.y = -1.0
        self.rect = pygame.Rect(self.location , (self.side, self.side))

        self.i = 0

        self.Color1 = pygame.Color(255, 232, 8)
        self.Color2 = pygame.Color(255, 0, 0)
        self.color_step = 0.1
        # print(self.side)
        


    def update(self,surface):

        
        color = self.Color1.lerp(self.Color2, self.i)
        self.i += self.color_step
        if self.i > 1.0:
            self.i = 1.0

        self.location += self.velocity
        self.side -= 0.1
        self.velocity.y = random.randint(0, 10)/15 - 1
        if math.fabs(self.velocity.x) > 0:

            if self.velocity.x > 0:

                self.velocity.x -= 0.05
            else:
                self.velocity.x += 0.05

        pygame.draw.rect(surface, color, pygame.Rect(
            self.location, (int(self.side), int(self.side))))

        new_location = self.location - pygame.Vector2(self.side*0.5, self.side*0.5)
        surface.blit(self.glow(self.side*2, (20, 20, 20)),
                    new_location, special_flags=pygame.BLEND_RGB_ADD)




    def toosmall(self):

        if self.side <= 2:
            return True
        else:
            return False

    def glow(self, radius, color):

        surf = pygame.Surface((int(radius * 2), int(radius * 2)))
        pygame.draw.circle(
            surf, color, (int(radius/2), int(radius/2)), int(radius/2))
        surf.set_colorkey((0, 0, 0))
        # surf = pygame.Surface((int(radius * 2), int(radius * 2)))
        # pygame.draw.rect(surf, color, pygame.Rect((0, 0), (int(radius * 2), int(radius * 2)))

        # surf.set_colorkey((0, 0, 0))

        return surf


class Fire:

    def __init__(self):
        
        self.particles = []
        self.tile_length = shared.TILESIZE * shared.SCALE # tile side is hard coded needs to be changed
        self.fire_surface = pygame.Surface((self.tile_length, self.tile_length*2 ))
        self.fire_surface.set_colorkey((0, 0, 0))
        self.RATE = 4
        self.counter = 0

        self.glow_radius = shared.TILESIZE * shared.SCALE 
        self.glow = pygame.Surface((self.glow_radius*2, self.glow_radius*2))
        self.glow.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.glow, (20, 20, 20), (self.glow_radius, self.glow_radius), self.glow_radius)
        self.phase = 0


    def update(self, surface, location):
        
        if self.counter % self.RATE == 0:

            self.fire_surface.fill((0, 0, 0))
            self.particles.append(Particles())

            for index, p in sorted(enumerate(self.particles),reverse =True):

                if p.toosmall():

                    self.particles.pop(index)

                else:

                    p.update(self.fire_surface)

        surface.blit(self.fire_surface, (location[0], location[1] - (
            self.tile_length) + 2*shared.SCALE), special_flags=pygame.BLEND_RGB_ADD)
        

        
        surface.blit(self.glow, (location[0]- self.glow_radius * 0.5, location[1] - (self.tile_length) + self.glow_radius * 0.5), special_flags=pygame.BLEND_RGB_ADD)
        
        
        self.counter = self.counter + 1
        

        
