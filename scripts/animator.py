
import pygame
import os
import shared


class Animation:

    def __init__(self,directory,typedir,frame_diff):

        self.name = typedir
        self.player_image = []
        self.directory = os.path.join(directory,typedir)

        self.filenames = sorted(os.listdir(self.directory))
        self.total_frames = len(self.filenames)
        self.frame_diff = frame_diff
        self.scale = shared.SCALE * 0.5
        self.frame = 1
        self.frame_gap = 1
        

        for filename in self.filenames:

            destination_file = os.path.join(self.directory, filename)

            temp_image = pygame.image.load(destination_file).convert()
            temp_image.set_colorkey((0, 0, 0))

            temp_image = pygame.transform.scale(
                temp_image, (int(temp_image.get_width() * self.scale), int(temp_image.get_height() * self.scale)))

            self.player_image.append(temp_image)


    
    def updateFrame(self):

        self.frame_gap = self.frame_gap + 1
        if self.frame_gap % self.frame_diff == 0:

            self.frame = self.frame + 1

        if self.frame > self.total_frames:

            self.frame = 1

    def getInstance(self):

        return self

    def getFrame(self):
        
        return self.player_image[self.frame-1]




class Animator:

    state = "idle"

    def __init__(self, directory):


        self.frame = 1
        self.frame_gap = 1

        # walk_directory = os.path.join(directory, "walk")
        # idle_directory = os.path.join(directory, "idle")

        self.walk_animation = Animation(directory,"walk",8)
        self.idle_animation = Animation(directory,"idle2",2)
        self.jump_animation  = Animation(directory,"jump",1)
        self.fall_animation = Animation(directory, "fall", 1)
        self.run_animation = Animation(directory, "run", 1)
        self.drop_animation = Animation(directory, "drop", 1)
    



    def frameRender(self):

        if self.state == "walk":
            anim = self.walk_animation.getInstance()

        elif self.state == "idle":
            anim = self.idle_animation.getInstance()
        
        elif self.state == "jump":
            anim = self.jump_animation.getInstance()
        
        elif self.state == "fall":
            anim = self.fall_animation.getInstance()

        elif self.state == "run":
            anim = self.run_animation.getInstance()

        elif self.state == "drop":
            anim = self.drop_animation.getInstance()
            print("drop")


        player_image = anim.getFrame()        
        anim.updateFrame()

        return player_image

    
    def changeState(self,new_state):

        if not (self.state == new_state):

            self.state = new_state
            
            # self.frame = 1


