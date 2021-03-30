import pygame
import os
import shared


class Mask:

    def __init__(self, location):

        self.dir = location

        self.dark_color = (50,50,50)

        self.light_mask = pygame.image.load(
            os.path.join(location, "alpha_mask.png")).convert()
        self.light_mask = pygame.transform.scale(self.light_mask, (100, 100))
        self.light_mask.set_colorkey((0, 0, 0))

        self.dark_mask = pygame.Surface(
            (shared.GAMEWINDOW_W, shared.GAMEWINDOW_H))
        pygame.draw.rect(self.dark_mask, self.dark_color, pygame.Rect(
            (0, 0), (shared.GAMEWINDOW_W, shared.GAMEWINDOW_H)))

    def apply_darkmask(self,surface):

        surface.blit(self.dark_mask, (0, 0),special_flags=pygame.BLEND_RGB_SUB)

    def apply_lightmask(self, surface, centerpos):

        surface.blit(self.light_mask, (centerpos - (self.light_mask.get_width()*0.5,self.light_mask.get_height()*0.5)), special_flags=pygame.BLEND_RGB_ADD)
