from window import *
from programlogic import *

class application:
    def __init__(self, title: str, dim_width: int, dim_height: int):
        self.title = title
        self.dimensions = (dim_width, dim_height)
        self.wd = window("Robot PID Test", (200, 200, 200), self.dimensions[0], self.dimensions[1])
        self.pl = programlogic()
        self.isRunning = self.wd.isRunning
        self.isPaused = False
        self.wait_time = 0.010
    
    def tick(self):
        
        self.process_inputs()
        if not self.isRunning: return
        if not self.isPaused:
            self.pl.tick()
            self.wd.update(self.pl.objects_list)

    dimensions = [640, 480]

    def process_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pl.icebot.set_rotation(self.pl.icebot.get_rotation() + 5.0)
        if keys[pygame.K_RIGHT]:
            self.pl.icebot.set_rotation(self.pl.icebot.get_rotation() - 5.0)
        if keys[pygame.K_SPACE]:
            if self.isPaused: self.isPaused = False
            else: self.isPaused = True

    def quit(self):
        self.wd.quit()
        self.isRunning = False