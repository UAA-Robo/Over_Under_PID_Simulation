import pygame as pygame
import objects.objects as obj

class programlogic:
    def __init__(self):
        """
        @brief    The program handling, controls program objects and event functions.
        """
        self.isRunning = True

        self.setup()

    def tick(self):
        """
        @brief    Runs all functions in the program necessary in one iteration
        """
        self.icebot.move()

        self.objects_list.update()
       
    def setup(self):
        """
        @brief    Function to setup specific programlogic class components for this program, 
                  like objects.
        """
        self.objects_list = pygame.sprite.Group()

        # Background Object
        self.background = obj.Sprite(800, 800, 400, 400, 0.0, -1, "background.png", "Background")
        self.objects_list.add(self.background)

        # Robot Object
        self.icebot = obj.Robot(64, 64, 400, 775, 90.0, 4.0, 1, "Robot.png", "Test Robot")
        self.objects_list.add(self.icebot)

        # Vertical Line Object
        self.vertical_line = obj.Sprite(800, 2, 400, 400, 0.0, 0, "Equilibrium.png", "Vertical Line")
        self.objects_list.add(self.vertical_line)



    