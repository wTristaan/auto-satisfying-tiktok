import os
import pygame
 
class VideoRecorder:
    def __init__(self):
        self.path = os.path.join("auto_recorder", "screenshots")
        self.name = "capture"
        self.frame = 0
 
        try:
            os.makedirs(self.path)
        except OSError:
            pass

        self.clear_screenshots()
    
    def make_png(self, screen):
        self.frame += 1
        fullpath = self.path + "/" + self.name + "%08d.png"%self.frame
        pygame.image.save(screen, fullpath)

    def clear_screenshots(self):
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            for filename in filenames:
                if filename.__contains__(".png"):
                    os.remove(os.path.join(dirpath, filename))