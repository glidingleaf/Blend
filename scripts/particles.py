import pygame
import random
import math


class Particles:

    def __init__(self):

        self.velocity = pygame.math.Vector2(0, 0)
        self.location = pygame.Vector2(8,24)
        self.velocity.x = random.randint(-10, 10)/10
        self.velocity.y = -1.0
        self.side = random.randint(3, 5)
        self.rect = pygame.Rect(self.location, (self.side, self.side))

        self.i = 0

        self.Color1 = pygame.Color(255, 232, 8)
        self.Color2 = pygame.Color(255, 0, 0)
        self.color_step = 0.1


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
        self.fire_surface = pygame.Surface((16, 32))
        self.fire_surface.set_colorkey((0, 0, 0))
        self.RATE = 4
        self.counter = 0



    def update(self, surface, location):
        
        if self.counter % self.RATE == 0:

            self.fire_surface.fill((0, 0, 0))
            self.particles.append(Particles())

            for index, p in sorted(enumerate(self.particles),reverse =True):

                if p.toosmall():

                    self.particles.pop(index)

                else:

                    p.update(self.fire_surface)

        surface.blit(self.fire_surface, (location[0] + 5, location[1] - 5))
        
        self.counter = self.counter + 1



        
