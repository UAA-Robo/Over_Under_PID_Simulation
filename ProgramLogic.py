import pygame as pygame
import objects.objects as obj

class ProgramLogic:
    def __init__(self, field_width: int, field_height: int, offset: tuple):
        """
        @brief    The program handling, controls program objects and event functions.
        @param field_width    The width of the available space to plot.
        @param field_height    The height of the available space to plot.
        @param offset    The x and y offset from the corner of the screen to set the local
                         coordinate axii.
        """
        self.isRunning = True

        self.setup()

    def tick(self, time_passed: int):
        """
        @brief    Runs all functions in the program necessary in one iteration.
        @param time_passed    The time passed since last execution.
        """
        self.icebot.move()
        self.text_list.clear()
        self.speedometer.text = "Speed: " + str(self.icebot.moved_distance / time_passed)
        self.text_list.append(self.speedometer)

        self.objects_list.update()

    def setup(self):
        """
        @brief    Function to setup specific programlogic class components for this program, 
                  like objects.
        """
        self.objects_list = pygame.sprite.Group()
        self.text_list = []

        # Background Object
        self.background = obj.Sprite(800, 800, 400, 400, 0.0, -1, "background.png", "Background")
        self.objects_list.add(self.background)

        # Robot Object
        self.icebot = obj.Robot(64, 64, 400, 775, 90.0, 4.0, 1, "Robot.png", "Test Robot")
        self.objects_list.add(self.icebot)

        # Vertical Line Object
        self.vertical_line = obj.Sprite(800, 2, 400, 400, 0.0, 0, "Equilibrium.png", "Vertical Line")
        self.objects_list.add(self.vertical_line)

        self.speedometer = obj.Text("", 50, 50)
        self.text_list.append(self.speedometer)



    